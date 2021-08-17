import styles from "./Navbar.module.scss";

import Link from "next/link";
import Navlink from "./NavLink";

import { useContext } from "react";
import AuthContext from "contexts/auth";

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
              ) : user ? (
                <a onClick={signOut}>Logout</a>
              ) : (
                <a onClick={signIn}>Login</a>
              )}
            </li>
          </ul>
        </nav>
      </div>
    </div>
  );
}
