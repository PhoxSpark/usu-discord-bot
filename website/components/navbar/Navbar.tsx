import styles from "./Navbar.module.scss";

import Link from "next/link";
import Navlink from "./NavLink";

import { useContext } from "react";
import AuthContext from "contexts/auth";
import Input from "components/input/Input";

export default function Navbar() {
  const { user, isLoading, signIn, signOut } = useContext(AuthContext);

  return (
    <div className={`${styles.background}`}>
      <div className={`${styles.navbar} container`}>
        <Link href="/">
          <h1>Usu</h1>
        </Link>
        <nav>
          <ul>
            <Navlink href="/">Home</Navlink>
            <li>
              {isLoading ? (
                <p>Loading...</p>
              ) : !user ? (
                <Input type="button" value="Login" onClick={signIn}/>
              ) : (
                <Input type="button" value="Logout" onClick={signOut}/>
              )}
            </li>
          </ul>
        </nav>
      </div>
    </div>
  );
}
