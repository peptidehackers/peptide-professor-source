import React from "react";
import "./App.css";
import { Routes, Route } from "react-router-dom";
import { HelmetProvider } from "react-helmet-async";
import { Analytics } from '@vercel/analytics/react';
import { SpeedInsights } from '@vercel/speed-insights/react';
import InteractiveHomepage from "./components/InteractiveHomepage";
import CompanyPages from "./pages/CompanyPages";
import CalculatorsPage from "./pages/CalculatorsPage";
import BlogPageStatic from "./pages/BlogPageStatic";
import BlogPostDetailStatic from "./pages/BlogPostDetailStatic";
import { Toaster } from "./components/ui/toaster";
import { DataProvider } from "./contexts/DataContext";
import MetaTags from "./components/seo/MetaTags";
import SkipLinks from "./components/accessibility/SkipLinks";
import StructuredData from "./components/seo/StructuredData";
import LoadingFallback from "./components/LoadingFallback";
import { smartLazy, withLoadingMetrics } from "./utils/lazyImports";

// Advanced lazy-loaded calculator components with smart preloading
const BMICalculatorPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "bmi-calculator" */ "./pages/BMICalculatorPage"), ['/calculators']));
const ReconstitutionCalculatorFree = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "reconstitution-calc" */ "./pages/ReconstitutionCalculatorFree"), ['/calculators']));
const PeptideProtocolTool = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "protocol-tool" */ "./pages/PeptideProtocolTool"), ['/calculators']));
const TRTCalculatorPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "trt-calculator" */ "./pages/TRTCalculatorPage"), ['/calculators']));
const MelanotanCalculatorPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "melanotan-calc" */ "./pages/MelanotanCalculatorPage"), ['/calculators']));
// Resilient lazy import with retry logic
const retryImport = (factory, retries = 2, delay = 500) =>
  new Promise((resolve, reject) => {
    const attempt = (n) =>
      factory().then(resolve).catch(err => n ? setTimeout(() => attempt(n-1), delay) : reject(err));
    attempt(retries);
  });

const GLP1CalculatorPage = (process.env.REACT_APP_DISABLE_SPLIT === "true")
  ? require("./pages/GLP1CalculatorPage").default
  : withLoadingMetrics(smartLazy(() => retryImport(() =>
      import(/* webpackChunkName: "glp1-calculator" */ "./pages/GLP1CalculatorPage")
    ), ['/calculators']));
const ReconstitutionCalculatorPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "reconstitution-legacy" */ "./pages/ReconstitutionCalculatorPage")));

// Core page components with route-based preloading
const PeptidesPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "peptides-page" */ "./pages/PeptidesPage"), ['/peptides', '/']));
const ResearchPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "research-page" */ "./pages/ResearchPage"), ['/research', '/']));
const ResourcesPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "resources-page" */ "./pages/ResourcesPage")));
const AboutPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "about-page" */ "./pages/AboutPage")));
const FAQPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "faq-page" */ "./pages/FAQPage")));
const MedSpaFinderPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "med-spa-finder" */ "./pages/MedSpaFinderPage")));

// Peptide-specific components
const PeptideCompatibilityPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "peptide-compatibility" */ "./pages/PeptideCompatibilityPage"), ['/peptides']));
const PeptideInteractionsPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "peptide-interactions" */ "./pages/PeptideInteractionsPage"), ['/peptides']));
const PeptideDetailPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "peptide-detail" */ "./pages/PeptideDetailPage"), ['/peptide']));
const PeptidesBrowsePage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "peptides-browse" */ "./pages/PeptidesBrowsePage"), ['/peptides']));
const PeptideCategoryPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "peptide-category" */ "./pages/PeptideCategoryPage"), ['/peptides']));
const ResearchCategoryPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "research-category" */ "./pages/ResearchCategoryPage"), ['/research']));
const QuizResultsPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "quiz-results" */ "./pages/QuizResultsPage")));

// Blog components with lower priority loading
const BlogHomepage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "blog-home" */ "./blog/index.jsx")));
const BlogRouter = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "blog-router" */ "./components/BlogRouter")));

// Search components
const SearchResultsPage = withLoadingMetrics(smartLazy(() => import(/* webpackChunkName: "search-results" */ "./pages/SearchResultsPage")));

const Home = () => {
  // Enhanced website structured data for SEO
  const websiteStructuredData = {
    name: "Professor Peptides",
    alternateName: ["Professor Peptides", "Professor Peptides Research Platform"],
    description: "World's most comprehensive peptide research platform with 47+ peptides, professional calculators, and expert medical oversight",
    url: "https://www.professorpeptides.org",
    foundingDate: "2025",
    numberOfEmployees: "5-10",
    industry: "Medical Research & Education",
    founder: {
      "@type": "Person",
      "name": "Shawn Younai"
    },
    medicalAdvisor: {
      "@type": "Person", 
      "name": "Dr. Sheraz Ahmad",
      "jobTitle": "Medical Advisor",
      "description": "Board-Certified Family Medicine Physician specializing in Hormone Optimization and Peptide Therapy"
    },
    offers: [
      {
        "@type": "Offer",
        "name": "Peptide Database Access",
        "description": "Access to 47+ research peptides with comprehensive profiles",
        "price": "0",
        "priceCurrency": "USD"
      },
      {
        "@type": "Offer", 
        "name": "Professional Calculators",
        "description": "7+ medical-grade peptide and health calculators",
        "price": "0",
        "priceCurrency": "USD"
      }
    ],
    mainEntity: {
      "@type": "WebSite",
      "name": "Professor Peptides",
      "url": "https://www.professorpeptides.org",
      "potentialAction": {
        "@type": "SearchAction",
        "target": "https://www.professorpeptides.org/peptides?q={search_term_string}",
        "query-input": "required name=search_term_string"
      }
    }
  };

  return (
    <>
      <MetaTags 
        title="Professor Peptides - #1 Research Database & Calculator Platform | 47+ Peptides"
        description="World's most comprehensive peptide research platform. 47+ peptides, professional calculators, 190+ scientific citations. Expert medical oversight by Dr. Sheraz Ahmad, M.D. Free tools, safety guides, and evidence-based protocols for researchers worldwide."
        keywords="peptide research, peptide database, peptide calculators, research peptides, semaglutide, tirzepatide, BPC-157, peptide therapy, hormone optimization, GLP-1 calculator, BMI calculator, peptide safety, Dr Sheraz Ahmad, medical research platform"
        canonical="https://www.professorpeptides.org"
        type="website"
      />
      
      {/* Enhanced Structured Data for SEO */}
      <StructuredData type="website" data={websiteStructuredData} />
      <StructuredData type="organization" />
      <StructuredData type="medicalWebPage" data={{
        name: "Professor Peptides - Research Database",
        description: "Comprehensive peptide research platform with medical oversight",
        medicalAudience: ["Researchers", "Medical Professionals", "Scientists"],
        about: {
          "@type": "MedicalCondition",
          "name": "Peptide Research and Therapy"
        }
      }} />
      
      {/* FAQ Structured Data for SEO */}
      <script type="application/ld+json">
        {JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            {
              "@type": "Question",
              "name": "What is Professor Peptides?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Professor Peptides is the world's most comprehensive peptide research platform featuring 47+ research peptides, professional calculators, and medical oversight by Dr. Sheraz Ahmad, M.D."
              }
            },
            {
              "@type": "Question", 
              "name": "How many peptides are in the database?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "We feature 47+ research peptides across 13 categories including metabolic health, tissue repair, muscle growth, cognitive enhancement, and more."
              }
            },
            {
              "@type": "Question",
              "name": "Who provides medical oversight?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Dr. Sheraz Ahmad, M.D., a Board-Certified Family Medicine physician specializing in hormone optimization and peptide therapy, serves as our Medical Advisor."
              }
            }
          ]
        })}
      </script>
      
      <InteractiveHomepage />
    </>
  );
};

function App() {
  return (
    <HelmetProvider>
      <DataProvider>
        <SkipLinks />
        <div className="App">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/company/*" element={<CompanyPages />} />
              
              {/* Quiz Results */}
              <Route path="/quiz-results" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <QuizResultsPage />
                </React.Suspense>
              } />
              
              {/* Search Results */}
              <Route path="/search" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <SearchResultsPage />
                </React.Suspense>
              } />
              
              {/* Essential pages */}
              <Route path="/peptides" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <PeptidesPage />
                </React.Suspense>
              } />
              <Route path="/research" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <ResearchPage />
                </React.Suspense>
              } />
              <Route path="/research/:category" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <ResearchCategoryPage />
                </React.Suspense>
              } />
              
              {/* Blog routes - Dynamic loading */}
              <Route path="/blog" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <BlogPageStatic />
                </React.Suspense>
              } />
              <Route path="/blog/:slug" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <BlogPostDetailStatic />
                </React.Suspense>
              } />
              <Route path="/blog/*" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <BlogRouter />
                </React.Suspense>
              } />
              
              <Route path="/resources" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <ResourcesPage />
                </React.Suspense>
              } />
              <Route path="/about" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <AboutPage />
                </React.Suspense>
              } />
              <Route path="/med-spa-finder" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <MedSpaFinderPage />
                </React.Suspense>
              } />
              <Route path="/faq" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <FAQPage />
                </React.Suspense>
              } />
              
              {/* Calculator routes */}
              <Route path="/calculators" element={<CalculatorsPage />} />
              <Route path="/calculators/bmi" element={
                <React.Suspense fallback={<LoadingFallback type="calculator" />}>
                  <BMICalculatorPage />
                </React.Suspense>
              } />
              <Route path="/calculators/reconstitution" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <ReconstitutionCalculatorFree />
                </React.Suspense>
              } />
              <Route path="/calculators/fitness" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <ReconstitutionCalculatorFree />
                </React.Suspense>
              } />
              <Route path="/calculators/protocol" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <PeptideProtocolTool />
                </React.Suspense>
              } />
              <Route path="/calculators/trt" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <TRTCalculatorPage />
                </React.Suspense>
              } />
              <Route path="/calculators/melanotan" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <MelanotanCalculatorPage />
                </React.Suspense>
              } />
              <Route path="/calculators/glp1" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <GLP1CalculatorPage />
                </React.Suspense>
              } />
              
              {/* Peptide routes */}
              <Route path="/peptides/browse" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <PeptidesBrowsePage />
                </React.Suspense>
              } />
              <Route path="/peptides/:category" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <PeptideCategoryPage />
                </React.Suspense>
              } />
              <Route path="/peptide/:peptideId" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <PeptideDetailPage />
                </React.Suspense>
              } />
              <Route path="/peptides/interactions" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <PeptideInteractionsPage />
                </React.Suspense>
              } />
              <Route path="/peptides/compatibility" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <PeptideCompatibilityPage />
                </React.Suspense>
              } />
              
              {/* Legacy routes for backward compatibility */}
              <Route path="/reconstitution-calculator" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <ReconstitutionCalculatorPage />
                </React.Suspense>
              } />
              <Route path="/peptide-protocol-tool" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <PeptideProtocolTool />
                </React.Suspense>
              } />
              
              {/* New URL pattern: /{peptideName}/{category}/{blogname} - KEEP AT END */}
              <Route path="/:peptideName/:category/:blogname" element={
                <React.Suspense fallback={<LoadingFallback />}>
                  <BlogRouter />
                </React.Suspense>
              } />
            </Routes>
          <Toaster />
          <Analytics />
          <SpeedInsights />
        </div>
      </DataProvider>
    </HelmetProvider>
  );
}

export default App;