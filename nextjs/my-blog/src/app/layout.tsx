import './globals.css'
import Header from '@/components/Layout/Header';
import Footer from '@/components/Layout/Footer';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="flex flex-col min-h-screen">
        <Header />
        <main className="flex-grow container mx-auto px-4 pt-24 pb-12">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}