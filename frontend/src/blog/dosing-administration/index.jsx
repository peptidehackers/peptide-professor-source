import React from 'react';
import { Link } from 'react-router-dom';

const DosingAdministrationCategory = () => {
  const articles = [
    {
      title: 'Peptide Reconstitution: Step-by-Step Protocols',
      slug: 'peptide-reconstitution-step-by-step-protocols',
      summary: 'Comprehensive protocols for proper peptide reconstitution techniques, solvent selection, and contamination prevention in research settings.',
      date: '2025-01-15'
    },
    {
      title: 'Bacteriostatic Water vs Sterile Water in Research',
      slug: 'bacteriostatic-vs-sterile-water-research',
      summary: 'Scientific comparison of bacteriostatic and sterile water applications, preservation properties, and optimal selection criteria.',
      date: '2025-01-12'
    },
    {
      title: 'Subcutaneous Injection Techniques for Research',
      slug: 'subcutaneous-injection-techniques-research',
      summary: 'Research methodologies for subcutaneous administration, anatomical considerations, and technique optimization protocols.',
      date: '2025-01-10'
    },
    {
      title: 'Intramuscular vs Subcutaneous: Route Selection',
      slug: 'intramuscular-vs-subcutaneous-route-selection',
      summary: 'Comparative analysis of administration routes, absorption kinetics, and route selection criteria for research protocols.',
      date: '2025-01-08'
    },
    {
      title: 'Dosing Calculations: Mathematical Approaches',
      slug: 'dosing-calculations-mathematical-approaches',
      summary: 'Mathematical methodologies for accurate dosing calculations, concentration determinations, and measurement precision in research.',
      date: '2025-01-05'
    },
    {
      title: 'Timing Protocols: Optimizing Research Administration',
      slug: 'timing-protocols-optimizing-research-administration',
      summary: 'Research protocols for optimal timing strategies, circadian considerations, and schedule optimization in peptide studies.',
      date: '2025-01-03'
    },
    {
      title: 'Multiple Daily Dosing vs Single Dose Research',
      slug: 'multiple-daily-vs-single-dose-research',
      summary: 'Comparative research methodologies examining multiple daily versus single-dose protocols and their research implications.',
      date: '2024-12-30'
    },
    {
      title: 'Cycling Protocols in Long-Term Research Studies',
      slug: 'cycling-protocols-longterm-research-studies',
      summary: 'Research methodologies for cycling protocols, washout periods, and long-term study design considerations.',
      date: '2024-12-28'
    },
    {
      title: 'Combination Therapy Dosing Considerations',
      slug: 'combination-therapy-dosing-considerations',
      summary: 'Research protocols for combination therapy approaches, interaction considerations, and dosing optimization strategies.',
      date: '2024-12-25'
    },
    {
      title: 'Age and Weight Adjustments in Research Protocols',
      slug: 'age-weight-adjustments-research-protocols',
      summary: 'Research methodologies for age and weight-based adjustments, scaling factors, and demographic considerations.',
      date: '2024-12-22'
    },
    {
      title: 'Refrigeration and Storage During Active Research',
      slug: 'refrigeration-storage-active-research',
      summary: 'Storage protocols for reconstituted peptides, temperature maintenance, and stability preservation during active research.',
      date: '2024-12-20'
    },
    {
      title: 'Needle Selection and Safety in Research Settings',
      slug: 'needle-selection-safety-research-settings',
      summary: 'Research protocols for needle selection criteria, safety considerations, and equipment optimization for research applications.',
      date: '2024-12-18'
    },
    {
      title: 'Site Rotation Protocols for Repeated Injections',
      slug: 'site-rotation-protocols-repeated-injections',
      summary: 'Research methodologies for injection site rotation, tissue preservation, and optimal site selection in repeated administration.',
      date: '2024-12-15'
    },
    {
      title: 'Emergency Procedures for Adverse Reactions',
      slug: 'emergency-procedures-adverse-reactions',
      summary: 'Research safety protocols for adverse reaction management, emergency procedures, and response protocols in research settings.',
      date: '2024-12-12'
    },
    {
      title: 'Documentation Requirements for Research Administration',
      slug: 'documentation-requirements-research-administration',
      summary: 'Protocol documentation standards, record-keeping requirements, and standardized documentation practices for research studies.',
      date: '2024-12-10'
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-cyan-50 via-white to-cyan-50">
      <div className="container mx-auto px-4 py-8">
        <nav className="mb-8">
          <div className="flex items-center space-x-2 text-sm text-gray-600 mb-4">
            <Link to="/" className="hover:text-cyan-600">Home</Link>
            <span>/</span>
            <Link to="/blog" className="hover:text-cyan-600">Blog</Link>
            <span>/</span>
            <span>Dosing & Administration</span>
          </div>
        </nav>

        <div className="max-w-4xl mx-auto">
          <div className="bg-gradient-to-r from-cyan-600 to-cyan-800 text-white p-8 rounded-t-lg">
            <div className="flex items-center space-x-4 mb-4">
              <span className="text-3xl">💉</span>
              <span className="bg-cyan-500 bg-opacity-50 px-3 py-1 rounded-full text-sm">
                {articles.length} Articles
              </span>
            </div>
            <h1 className="text-3xl font-bold mb-4">Dosing & Administration Research</h1>
            <p className="text-cyan-100">
              Research methodologies and protocols for peptide dosing calculations, administration techniques, 
              and optimization strategies in controlled research environments.
            </p>
          </div>

          <div className="bg-white rounded-b-lg shadow-lg">
            <div className="p-8">
              <div className="space-y-6">
                {articles.map((article, index) => (
                  <Link
                    key={article.slug}
                    to={`/blog/dosing-administration/${article.slug}`}
                    className="block group"
                  >
                    <div className="border border-gray-200 rounded-lg p-6 hover:shadow-md transition-shadow">
                      <div className="flex justify-between items-start mb-3">
                        <h2 className="text-xl font-semibold text-gray-900 group-hover:text-cyan-600 transition-colors">
                          {article.title}
                        </h2>
                        <span className="text-sm text-gray-500 ml-4 flex-shrink-0">{article.date}</span>
                      </div>
                      <p className="text-gray-600 leading-relaxed mb-4">
                        {article.summary}
                      </p>
                      <div className="flex items-center text-cyan-600 group-hover:text-cyan-800 transition-colors">
                        <span>Read article</span>
                        <span className="ml-2 transform transition-transform group-hover:translate-x-1">→</span>
                      </div>
                    </div>
                  </Link>
                ))}
              </div>
            </div>

            <div className="bg-gray-50 p-6 border-t">
              <Link 
                to="/blog" 
                className="inline-flex items-center text-cyan-600 hover:text-cyan-800 transition-colors"
              >
                ← Back to Blog Categories
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DosingAdministrationCategory;