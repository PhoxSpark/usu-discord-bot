import { useContext } from "react";
import AuthContext from "contexts/auth";

export default function Home() {
  const { user, isLoading } = useContext(AuthContext);

  return (
    <div className={`container`}>
      {
        isLoading ? <p>Loading...</p> : <p>{user ? user.username : "Index page"}</p>
      }
    </div>
  );
}
