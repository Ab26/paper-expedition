import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Paper Expedition | AB's CV + NLP reading studio",
  description: "98 papers, 33 weeks. An interactive reading schedule from foundations to vision-language research.",
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
