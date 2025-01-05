// src/app/page.tsx
export default function Home() {
  return (
    <div className="max-w-4xl mx-auto px-4">
      {/* Hero Section */}
      <section className="text-center py-20">
        <h1 className="text-5xl font-bold mb-4 text-gray-800">Welcome to My Blog</h1>
        <p className="text-xl text-gray-600 max-w-2xl mx-auto">
          A place where I share my thoughts and experiences
        </p>
      </section>

      {/* Featured Posts */}
      <section className="mb-16">
        <h2 className="text-3xl font-bold mb-8 text-gray-800">Featured Posts</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
            <div className="p-6">
              <h3 className="text-xl font-semibold mb-3 text-gray-800">Sample Blog Post</h3>
              <p className="text-gray-600 mb-4">
                This is a preview of what your blog posts will look like...
              </p>
              <a 
                href="/blog/sample-post" 
                className="text-blue-600 hover:text-blue-800 font-medium inline-flex items-center group"
              >
                Read more 
                <span className="ml-2 group-hover:translate-x-1 transition-transform">→</span>
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Recent Posts */}
      <section className="mb-16">
        <h2 className="text-3xl font-bold mb-8 text-gray-800">Recent Posts</h2>
        <div className="space-y-8">
          <div className="border-b border-gray-200 pb-8">
            <h3 className="text-xl font-semibold mb-3 text-gray-800">Another Blog Post</h3>
            <p className="text-gray-600 mb-4">
              A preview of another blog post...
            </p>
            <a 
              href="/blog/another-post" 
              className="text-blue-600 hover:text-blue-800 font-medium inline-flex items-center group"
            >
              Read more 
              <span className="ml-2 group-hover:translate-x-1 transition-transform">→</span>
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}