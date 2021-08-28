import styles from "./Navbar.module.scss";

import Link from "next/link";
import Navlink from "./NavLink";

import { useContext, useState, useRef } from "react";
import useOutsideClick from "hooks/useOutsideClick";

import AuthContext from "contexts/auth";
import Input from "components/input/Input";
import Skeleton from "components/skeleton/Skeleton";

export default function Navbar() {
  const { user, signIn, signOut } = useContext(AuthContext);
  const [imgLoading, setImgLoading] = useState(true);
  const [userMenuVisible, setUserMenuVisibility] = useState(false);
  const ref = useRef();

  useOutsideClick(ref, () => {
    if (userMenuVisible) setUserMenuVisibility(false);
  });

  const userPreview = () => {
    return (
      <div className={styles.userPreview} onClick={() => setUserMenuVisibility(!userMenuVisible)}>
        {imgLoading && <Skeleton type="circle" width="38px" height="38px" />}

        <img
          className={styles.userImg}
          style={{ display: imgLoading ? "none" : "block" }}
          src={`https://cdn.discordapp.com/avatars/${user.id}/${user.avatar}.gif`}
          onLoad={() => setImgLoading(false)}
        />
      </div>
    );
  };

  return (
    <div className={`${styles.background}`}>
      <div className={`container`}>
        <div className={`${styles.navbar}`}>
          <Link href="/">
            <h1>Usu</h1>
          </Link>
          <nav>
            <ul>
              <Navlink href="/">Home</Navlink>
              <li>
                {user ? (
                  userPreview()
                ) : (
                  <Input type="button" onClick={signIn} value="Login" />
                )}
              </li>
            </ul>
          </nav>
        </div>
        {
          user &&
            userMenuVisible &&
              <div className={styles.userMenu} ref={ref}>
                <ul>
                  <li onClick={signOut}>Logout</li>
                </ul>
              </div>
        }
        
      </div>
    </div>
  );
}
