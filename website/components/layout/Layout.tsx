import { useContext } from "react";
import AuthContext from "contexts/auth";

import Navbar from "components/navbar/Navbar";

interface Props {
  children: React.ReactNode;
}

export default function Layout(props: Props) {
  const { isLoading } = useContext(AuthContext);
  return isLoading ? (
    <h1 style={{textAlign: "center", fontSize: "40px", marginTop: "20px"}}>Loading...</h1>
  ) : (
    <>
      <Navbar />
      <main>{props.children}</main>
    </ >
  );
}
