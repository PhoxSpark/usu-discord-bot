import "styles/globals.scss";

import type { AppProps } from "next/app";

import { AuthProvider } from "contexts/auth";
import Navbar from "components/navbar/Navbar";

import Layout from "components/layout/Layout";

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <AuthProvider>
      <Layout>
        <Component {...pageProps} />
      </Layout>
    </AuthProvider>
  );
}

export default MyApp;
