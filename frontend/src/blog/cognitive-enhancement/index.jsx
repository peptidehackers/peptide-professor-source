import React from 'react';
import { Link } from 'react-router-dom';

const CognitiveEnhancementCategory = () => {
  const articles = [
    {
      title: 'Nootropic Peptides Research Overview',
      slug: 'nootropic-peptides-research-overview',
      summary: 'Comprehensive analysis of nootropic peptide research, mechanisms, and applications in cognitive enhancement studies.',
      date: '2025-01-15'
    },
    {
      title: 'Cognitive Function Assessment Methods',
      slug: 'cognitive-function-assessment-methods',
      summary: 'Research methodologies and assessment protocols for evaluating cognitive function in peptide studies.',
      date: '2025-01-12'
    },
    {
      title: 'Neuroprotective Peptide Mechanisms',
      slug: 'neuroprotective-peptide-mechanisms',
      summary: 'Scientific exploration of neuroprotective pathways and mechanisms in peptide-based neurological research.',
      date: '2025-01-10'
    },
    {
      title: 'Memory Enhancement Research Protocols',
      slug: 'memory-enhancement-research-protocols',
      summary: 'Analysis of research protocols and methodologies in memory enhancement peptide studies.',
      date: '2025-01-08'
    },
    {
      title: 'Neuroplasticity Peptide Applications',
      slug: 'neuroplasticity-peptide-applications',
      summary: 'Research applications of peptides in neuroplasticity studies and synaptic modulation research.',
      date: '2025-01-05'
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-white to-purple-50">
      <div className="container mx-auto px-4 py-8">
        <nav className="mb-8">
          <div className="flex items-center space-x-2 text-sm text-gray-600 mb-4">
            <Link to="/" className="hover:text-purple-600">Home</Link>
            <span>/</span>
            <Link to="/blog" className="hover:text-purple-600">Blog</Link>
            <span>/</span>
            <span>Cognitive Enhancement</span>
          </div>
        </nav>

        <div className="max-w-4xl mx-auto">
          <div className="bg-gradient-to-r from-purple-600 to-purple-800 text-white p-8 rounded-t-lg">
            <div className="flex items-center space-x-4 mb-4">
              <span className="text-3xl">🧠</span>
              <span className="bg-purple-500 bg-opacity-50 px-3 py-1 rounded-full text-sm">
                {articles.length} Articles
              </span>
            </div>
            <h1 className="text-3xl font-bold mb-4">Cognitive Enhancement Research</h1>
            <p className="text-purple-100">
              Scientific research and analysis of cognitive enhancement peptides, nootropics, 
              and neuroplasticity compounds in neurological studies.
            </p>
          </div>

          <div className="bg-white rounded-b-lg shadow-lg">
            <div className="p-8">
              <div className="space-y-6">
                {articles.map((article, index) => (
                  <Link
                    key={article.slug}
                    to={`/blog/cognitive-enhancement/${article.slug}`}
                    className="block group"
                  >
                    <div className="border border-gray-200 rounded-lg p-6 hover:shadow-md transition-shadow">
                      <div className="flex justify-between items-start mb-3">
                        <h2 className="text-xl font-semibold text-gray-900 group-hover:text-purple-600 transition-colors">
                          {article.title}
                        </h2>
                        <span className="text-sm text-gray-500 ml-4 flex-shrink-0">{article.date}</span>
                      </div>
                      <p className="text-gray-600 leading-relaxed mb-4">
                        {article.summary}
                      </p>
                      <div className="flex items-center text-purple-600 group-hover:text-purple-800 transition-colors">
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
                className="inline-flex items-center text-purple-600 hover:text-purple-800 transition-colors"
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

export default CognitiveEnhancementCategory;