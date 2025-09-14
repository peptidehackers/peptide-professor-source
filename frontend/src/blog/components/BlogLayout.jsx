import React from 'react';
import { Link } from 'react-router-dom';

const BlogLayout = ({ title, category, date, slug, children }) => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-blue-50">
      <div className="container mx-auto px-4 py-8">
        <nav className="mb-8">
          <div className="flex items-center space-x-2 text-sm text-gray-600 mb-4">
            <Link to="/" className="hover:text-blue-600">Home</Link>
            <span>/</span>
            <Link to="/blog" className="hover:text-blue-600">Blog</Link>
            <span>/</span>
            <Link to={`/blog/${category.toLowerCase().replace(/\s+/g, '-')}`} className="hover:text-blue-600">
              {category}
            </Link>
          </div>
        </nav>

        <div className="max-w-4xl mx-auto bg-white rounded-lg shadow-lg overflow-hidden">
          <div className="bg-gradient-to-r from-blue-600 to-blue-800 text-white p-8">
            <div className="flex items-center space-x-4 mb-4">
              <span className="bg-blue-500 bg-opacity-50 px-3 py-1 rounded-full text-sm">
                {category}
              </span>
              <span className="text-blue-200">{date}</span>
            </div>
            <h1 className="text-3xl font-bold mb-4">{title}</h1>
          </div>

          <div className="p-8">
            {children}
          </div>

          <div className="bg-gray-50 p-8 border-t">
            <div className="flex justify-between items-center">
              <Link 
                to="/blog" 
                className="inline-flex items-center text-blue-600 hover:text-blue-800 transition-colors"
              >
                ← Back to Blog
              </Link>
              <div className="flex space-x-4">
                <Link 
                  to={`/blog/${category.toLowerCase().replace(/\s+/g, '-')}`}
                  className="text-blue-600 hover:text-blue-800 transition-colors"
                >
                  More in {category}
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BlogLayout;