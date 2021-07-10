import "styles/globals.scss";

import type { AppProps } from "next/app";

import { AuthProvider } from "contexts/auth";
import Navbar from "components/navbar/Navbar";

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <AuthProvider>
      <Navbar />
      <main>
        <Component {...pageProps} />
      </main>
    </AuthProvider>
  );
}

export default MyApp;
