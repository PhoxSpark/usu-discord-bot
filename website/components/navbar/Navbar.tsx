import styles from "./Navbar.module.scss";

import Link from "next/link";
import Navlink from "./NavLink";
import { useRouter } from "next/router";
import Cookies from "universal-cookie";

export default function Navbar() {
  const router = useRouter();
  const stateGenerator = (length) => {
    var result = "";
    var characters =
      "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
  }

  const discordLogin = () => {
    const cookies = new Cookies();
    const getState = stateGenerator(50);
    cookies.set("state", getState);

    router.push(`https://discord.com/api/oauth2/authorize?client_id=${process.env.CLIENT_ID}&redirect_uri=${process.env.REDIRECT_URI}&response_type=code&scope=${process.env.SCOPE}&state=${getState}`)
  }

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
              <a onClick={discordLogin}>Login</a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  );
}
