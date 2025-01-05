export default function Header() {
    return (
      <header className="fixed top-0 w-full bg-white shadow-md z-50">
        <div className="container mx-auto px-4 py-4">
          <nav className="flex items-center justify-between">
            <h1 className="text-2xl font-bold">TOYO Blog</h1>
            <ul className="flex space-x-6">
              <li><a href="/" className="hover:text-gray-600">Home</a></li>
              <li><a href="/blog" className="hover:text-gray-600">Blog</a></li>
              <li><a href="/about" className="hover:text-gray-600">About</a></li>
            </ul>
          </nav>
        </div>
      </header>
    );
  }