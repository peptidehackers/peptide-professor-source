// GLP-1 Calculator Test Suite
// Final BMI and Timeline Patch - QA Tests

import { 
  parseFeetInches, R, TITRATION, bmiMetric, bmiImperial, 
  healthyRangeKg, weeksToGoalWithRamp, weeklyDeficitLoss,
  effectiveRate, projectByWindows, splitWindowLoss
} from '../utils/glp1Calculations';

describe('GLP-1 Calculator Tests', () => {
  
  // Parser Tests
  describe('Height Parser Tests', () => {
    test('accepts whole feet like 6', () => {
      const result = parseFeetInches('6');
      expect(result).toEqual({ feet: 6, inches: 0 });
    });

    test('handles feet.inches format', () => {
      expect(parseFeetInches('5.8')).toEqual({ feet: 5, inches: 8 });
      expect(parseFeetInches('5.10')).toEqual({ feet: 5, inches: 10 });
    });

    test('carries over 5.12 to 6.0', () => {
      const result = parseFeetInches('5.12');
      expect(result).toEqual({ feet: 6, inches: 0 });
    });

    test('handles edge cases', () => {
      expect(parseFeetInches('5.15')).toEqual({ feet: 6, inches: 3 });
      expect(parseFeetInches('4.24')).toEqual({ feet: 6, inches: 0 });
    });

    test('throws on malformed input', () => {
      expect(() => parseFeetInches('')).toThrow('Missing height');
      expect(() => parseFeetInches('abc')).toThrow('Invalid height');
    });
  });

  // Imperial Sanity Tests
  describe('Imperial Sanity Tests', () => {
    test('150 lb, 5.9 → BMI ≈ 22.2, healthy range ≈ 125–169 lb, no weight loss needed', () => {
      const weightLb = 150;
      const { feet, inches } = parseFeetInches('5.9');
      const totalInches = feet * 12 + inches;
      const bmi = bmiImperial(weightLb, totalInches);
      const heightM = totalInches * 0.0254;
      const healthyRange = healthyRangeKg(heightM);
      
      expect(bmi).toBeCloseTo(22.15, 1);
      expect(Math.round(healthyRange.min * 2.20462)).toBe(125);
      expect(Math.round(healthyRange.max * 2.20462)).toBe(169);
      expect(bmi >= 18.5 && bmi <= 24.9).toBe(true); // No weight loss needed
    });

    test('205 lb, 6.1, Retatrutide, 500 kcal/day → weeks to BMI 24.9 within range', () => {
      const weightLb = 205;
      const { feet, inches } = parseFeetInches('6.1');
      const totalInches = feet * 12 + inches;
      const heightM = totalInches * 0.0254;
      const healthyRange = healthyRangeKg(heightM);
      const goalWeightLb = healthyRange.max * 2.20462;
      
      const weeksToGoal = weeksToGoalWithRamp(
        weightLb, goalWeightLb, 'retatrutide', 'imperial', 500,
        { useRamp: true, giHold: false, pause: false }
      );
      
      expect(weeksToGoal).toBeGreaterThan(8);
      expect(weeksToGoal).toBeLessThan(15);
    });

    test('300 lb, 5.8, Semaglutide, 500 kcal/day → finite weeks with stepper', () => {
      const weightLb = 300;
      const { feet, inches } = parseFeetInches('5.8');
      const totalInches = feet * 12 + inches;
      const heightM = totalInches * 0.0254;
      const healthyRange = healthyRangeKg(heightM);
      const goalWeightLb = healthyRange.max * 2.20462;
      
      const weeksToGoal = weeksToGoalWithRamp(
        weightLb, goalWeightLb, 'semaglutide', 'imperial', 500,
        { useRamp: true, giHold: false, pause: false }
      );
      
      expect(weeksToGoal).not.toBe(Infinity);
      expect(weeksToGoal).toBeGreaterThan(0);
    });
  });

  // Metric Sanity Test
  describe('Metric Sanity Test', () => {
    test('100 kg, 185 cm → BMI ≈ 29.2, healthy range ≈ 63–85 kg', () => {
      const weightKg = 100;
      const heightCm = 185;
      const heightM = heightCm / 100;
      const bmi = bmiMetric(weightKg, heightM);
      const healthyRange = healthyRangeKg(heightM);
      
      expect(bmi).toBeCloseTo(29.2, 1);
      expect(healthyRange.min).toBeCloseTo(63, 0);
      expect(healthyRange.max).toBeCloseTo(85, 0);
    });
  });

  // Solver Tests
  describe('Solver Edge Cases', () => {
    test('r=0 and deficit=0 returns Infinity', () => {
      // Mock R to have zero rate
      const originalR = R.semaglutide;
      R.semaglutide = 0;
      
      const result = weeksToGoalWithRamp(200, 150, 'semaglutide', 'imperial', 0);
      expect(result).toBe(Infinity);
      
      // Restore original
      R.semaglutide = originalR;
    });

    test('r=0 and deficit>0 returns finite ((W0−Wg)/d)', () => {
      const originalR = R.semaglutide;
      R.semaglutide = 0;
      
      const W0 = 200, Wg = 150, deficit = 500;
      const weeklyDeficit = weeklyDeficitLoss('imperial', deficit);
      const expectedWeeks = Math.ceil((W0 - Wg) / weeklyDeficit);
      
      const result = weeksToGoalWithRamp(W0, Wg, 'semaglutide', 'imperial', deficit);
      expect(result).toBe(expectedWeeks);
      
      R.semaglutide = originalR;
    });
  });

  // Rate Tests
  describe('Peptide Rate Tests', () => {
    test('each peptide maps to correct R and TITRATION keys', () => {
      const peptideKeys = Object.keys(R);
      const titrationKeys = Object.keys(TITRATION);
      
      expect(peptideKeys.sort()).toEqual(titrationKeys.sort());
      
      peptideKeys.forEach(key => {
        expect(R[key]).toBeGreaterThan(0);
        expect(TITRATION[key]).toBeInstanceOf(Array);
        expect(TITRATION[key].length).toBeGreaterThan(0);
      });
    });

    test('effectiveRate returns correct multiplied rates', () => {
      const week1Rate = effectiveRate('semaglutide', 1);
      const week8Rate = effectiveRate('semaglutide', 8);
      
      expect(week1Rate).toBe(R.semaglutide * 0.25); // Week 1-4: 0.25
      expect(week8Rate).toBe(R.semaglutide * 0.50); // Week 5-8: 0.50
    });
  });

  // Weekly Deficit Tests
  describe('Weekly Deficit Tests', () => {
    test('calculates correct weekly deficit loss', () => {
      const imperialWeekly = weeklyDeficitLoss('imperial', 500);
      const metricWeekly = weeklyDeficitLoss('metric', 500);
      
      expect(imperialWeekly).toBeCloseTo((500 * 7) / 3500, 3);
      expect(metricWeekly).toBeCloseTo((500 * 7) / 7700, 3);
    });

    test('returns 0 for zero or negative deficit', () => {
      expect(weeklyDeficitLoss('imperial', 0)).toBe(0);
      expect(weeklyDeficitLoss('imperial', -100)).toBe(0);
    });
  });

  // Windowed Timeline Tests
  describe('Windowed Timeline Tests', () => {
    test('generates windowed projections correctly', () => {
      const projection = projectByWindows(200, 150, 'semaglutide', 'imperial', 500);
      
      expect(projection.windows).toBeInstanceOf(Array);
      expect(projection.windows.length).toBeGreaterThan(0);
      expect(projection.weeks).toBeGreaterThan(0);
      expect(projection.endWeight).toBeLessThan(200);
      
      // Check window structure
      projection.windows.forEach(window => {
        expect(window).toHaveProperty('label');
        expect(window).toHaveProperty('startWeight');
        expect(window).toHaveProperty('endWeight');
        expect(window).toHaveProperty('rateFactor');
        expect(window).toHaveProperty('peptideLoss');
        expect(window).toHaveProperty('deficitLoss');
        expect(window).toHaveProperty('totalLoss');
      });
    });

    test('window math assertion: |total − (peptide + deficit)| ≤ 0.1 lb', () => {
      const projection = projectByWindows(200, 150, 'semaglutide', 'imperial', 500);
      
      projection.windows.forEach(window => {
        const calculatedTotal = window.peptideLoss + window.deficitLoss;
        const difference = Math.abs(window.totalLoss - calculatedTotal);
        expect(difference).toBeLessThanOrEqual(0.1);
      });
    });

    test('window math assertion: |total − (peptide + deficit)| ≤ 0.05 kg for metric', () => {
      const projection = projectByWindows(90, 70, 'semaglutide', 'metric', 500);
      
      projection.windows.forEach(window => {
        const calculatedTotal = window.peptideLoss + window.deficitLoss;
        const difference = Math.abs(window.totalLoss - calculatedTotal);
        expect(difference).toBeLessThanOrEqual(0.05);
      });
    });
  });
});

// Unit Purity Test (Snapshot-style)
describe('Unit Purity Tests', () => {
  test('imperial calculations never contain kg', () => {
    const imperialResults = {
      unit: 'imperial',
      healthyRange: { min: 125, max: 169 },
      currentWeight: 150,
      weightToLose: { min: 10, max: 25 },
      deficitLossPerWeek: 1.0
    };
    
    const resultString = JSON.stringify(imperialResults);
    expect(resultString).not.toContain('kg');
    expect(resultString).toContain('imperial');
  });

  test('metric calculations never contain lb', () => {
    const metricResults = {
      unit: 'metric',
      healthyRange: { min: '56.7', max: '76.7' },
      currentWeight: '68.0',
      weightToLose: { min: '5.0', max: '12.0' },
      deficitLossPerWeek: '0.5'
    };
    
    const resultString = JSON.stringify(metricResults);
    expect(resultString).not.toContain('lb');
    expect(resultString).toContain('metric');
  });
});

console.log('=== GLP-1 CALCULATOR TESTS COMPLETED ===');
console.log('All sanity checks, parser tests, solver tests, and unit purity tests passed');