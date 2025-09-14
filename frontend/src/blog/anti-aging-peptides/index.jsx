import React from 'react';
import { Link } from 'react-router-dom';

const AntiAgingPeptides = () => {
  const articles = [
    {
      title: 'Epithalon: Telomerase Activation Research and Longevity Studies',
      slug: 'epithalon-telomerase-activation-research',
      excerpt: 'Research examination of epithalon\'s telomerase activation mechanisms and longevity applications in clinical study protocols.',
      date: '2025'
    },
    {
      title: 'GHK-Cu: Copper Peptide Research in Tissue Regeneration',
      slug: 'ghk-cu-copper-peptide-tissue-research',
      excerpt: 'Clinical research on GHK-Cu copper peptide applications in tissue regeneration and anti-aging research protocols.',
      date: '2025'
    },
    {
      title: 'Thymalin: Thymus Extract Peptide Immune Research',
      slug: 'thymalin-thymus-extract-immune-research',
      excerpt: 'Research insights into thymalin\'s immune system modulation properties and anti-aging research applications.',
      date: '2025'
    },
    {
      title: 'NAD+ Precursors and Peptide Combinations in Aging Research',
      slug: 'nad-precursors-peptide-combinations-aging',
      excerpt: 'Clinical studies examining NAD+ precursor and peptide combination protocols in aging research applications.',
      date: '2025'
    },
    {
      title: 'Mitochondrial Peptides: SS-31 and Cellular Energy Research',
      slug: 'mitochondrial-peptides-ss31-cellular-research',
      excerpt: 'Research analysis of mitochondrial peptides like SS-31 in cellular energy optimization and anti-aging studies.',
      date: '2025'
    },
    {
      title: 'Pinealon: Neurological Anti-Aging Peptide Studies',
      slug: 'pinealon-neurological-anti-aging-studies',
      excerpt: 'Clinical research on pinealon\'s neurological protection properties and anti-aging research applications.',
      date: '2025'
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-blue-50">
      <div className="container mx-auto px-4 py-8">
        <nav className="mb-8">
          <div className="flex items-center space-x-2 text-sm text-gray-600 mb-4">
            <Link to="/" className="hover:text-blue-600">Home</Link>
            <span>/</span>
            <Link to="/blog" className="hover:text-blue-600">Blog</Link>
            <span>/</span>
            <span>Anti-Aging Peptides</span>
          </div>
        </nav>

        <div className="max-w-6xl mx-auto">
          <div className="bg-gradient-to-r from-yellow-600 to-yellow-800 text-white rounded-lg p-8 mb-12">
            <div className="flex items-center space-x-4 mb-6">
              <span className="text-4xl">⏳</span>
              <div>
                <h1 className="text-4xl font-bold mb-2">Anti-Aging Peptides</h1>
                <p className="text-yellow-200 text-lg">
                  Research insights on longevity peptides, cellular regeneration, and anti-aging clinical study applications
                </p>
              </div>
            </div>
            <div className="bg-yellow-500 bg-opacity-50 px-4 py-2 rounded-full inline-block">
              <span className="text-sm font-medium">{articles.length} Research Articles</span>
            </div>
          </div>

          <div className="grid gap-8 mb-12">
            {articles.map((article) => (
              <Link
                key={article.slug}
                to={`/blog/anti-aging-peptides/${article.slug}`}
                className="group block"
              >
                <div className="bg-white rounded-lg shadow-lg overflow-hidden transform transition-all duration-300 hover:scale-[1.02] hover:shadow-xl">
                  <div className="p-8">
                    <div className="flex items-start justify-between mb-4">
                      <div className="flex-1">
                        <h2 className="text-2xl font-bold text-gray-900 mb-3 group-hover:text-yellow-600 transition-colors">
                          {article.title}
                        </h2>
                        <p className="text-gray-600 leading-relaxed mb-4">
                          {article.excerpt}
                        </p>
                      </div>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-gray-500">{article.date}</span>
                      <span className="text-yellow-600 group-hover:text-yellow-800 transition-colors font-medium">
                        Read Research Article →
                      </span>
                    </div>
                  </div>
                </div>
              </Link>
            ))}
          </div>

          <div className="bg-white rounded-lg shadow-lg p-8 text-center">
            <h3 className="text-2xl font-bold text-gray-900 mb-4">Research Disclaimer</h3>
            <p className="text-gray-600 leading-relaxed max-w-4xl mx-auto">
              All anti-aging peptide research content is provided for educational and research purposes only. 
              This information is not intended as medical advice, diagnosis, or treatment recommendations. 
              Always consult with qualified healthcare professionals for medical guidance. The research discussed 
              may be preliminary, ongoing, or theoretical.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AntiAgingPeptides;