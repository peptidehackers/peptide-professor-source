import React from 'react';
import { Link } from 'react-router-dom';

const CosmeticPeptidesCategory = () => {
  const articles = [
    {
      title: 'Matrixyl (Palmitoyl Pentapeptide): Collagen Synthesis Research',
      slug: 'matrixyl-palmitoyl-pentapeptide-collagen-research',
      summary: 'Scientific analysis of Matrixyl\'s role in collagen synthesis and dermatological research applications.',
      date: '2025-01-15'
    },
    {
      title: 'Argireline: Muscle Contraction Peptide Cosmetic Studies',
      slug: 'argireline-muscle-contraction-cosmetic-studies',
      summary: 'Research examination of Argireline\'s mechanisms in muscle contraction modulation for cosmetic applications.',
      date: '2025-01-12'
    },
    {
      title: 'Copper Peptides in Dermatological Research Applications',
      slug: 'copper-peptides-dermatological-research',
      summary: 'Clinical research analyzing copper peptides in wound healing and skin regeneration studies.',
      date: '2025-01-10'
    },
    {
      title: 'Peptide Combinations in Anti-Aging Skincare Research',
      slug: 'peptide-combinations-anti-aging-skincare-research',
      summary: 'Research methodologies examining synergistic effects of combined peptides in anti-aging applications.',
      date: '2025-01-08'
    },
    {
      title: 'Bioavailability of Topical Peptides: Research Methodologies',
      slug: 'topical-peptides-bioavailability-research',
      summary: 'Scientific investigation of peptide penetration and bioavailability in topical formulation research.',
      date: '2025-01-05'
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-50 via-white to-pink-50">
      <div className="container mx-auto px-4 py-8">
        <nav className="mb-8">
          <div className="flex items-center space-x-2 text-sm text-gray-600 mb-4">
            <Link to="/" className="hover:text-pink-600">Home</Link>
            <span>/</span>
            <Link to="/blog" className="hover:text-pink-600">Blog</Link>
            <span>/</span>
            <span>Cosmetic Peptides</span>
          </div>
        </nav>

        <div className="max-w-4xl mx-auto">
          <div className="bg-gradient-to-r from-pink-600 to-pink-800 text-white p-8 rounded-t-lg">
            <div className="flex items-center space-x-4 mb-4">
              <span className="text-3xl">💄</span>
              <span className="bg-pink-500 bg-opacity-50 px-3 py-1 rounded-full text-sm">
                {articles.length} Articles
              </span>
            </div>
            <h1 className="text-3xl font-bold mb-4">Cosmetic Peptides Research</h1>
            <p className="text-pink-100">
              Scientific research and clinical analysis of cosmetic peptides including collagen modulators, 
              anti-aging compounds, and dermatological applications in skincare research.
            </p>
          </div>

          <div className="bg-white rounded-b-lg shadow-lg">
            <div className="p-8">
              <div className="space-y-6">
                {articles.map((article, index) => (
                  <Link
                    key={article.slug}
                    to={`/blog/cosmetic-peptides/${article.slug}`}
                    className="block group"
                  >
                    <div className="border border-gray-200 rounded-lg p-6 hover:shadow-md transition-shadow">
                      <div className="flex justify-between items-start mb-3">
                        <h2 className="text-xl font-semibold text-gray-900 group-hover:text-pink-600 transition-colors">
                          {article.title}
                        </h2>
                        <span className="text-sm text-gray-500 ml-4 flex-shrink-0">{article.date}</span>
                      </div>
                      <p className="text-gray-600 leading-relaxed mb-4">
                        {article.summary}
                      </p>
                      <div className="flex items-center text-pink-600 group-hover:text-pink-800 transition-colors">
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
                className="inline-flex items-center text-pink-600 hover:text-pink-800 transition-colors"
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

export default CosmeticPeptidesCategory;