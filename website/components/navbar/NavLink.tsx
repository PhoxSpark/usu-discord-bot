import Link from "next/link";

interface Props {
  href: string;
  as?: string;
  children: string;
}

export default function Navlink(props: Props) {
  return (
    <li>
      <Link href={props.href} as={props.as}>
        <a>{props.children}</a>
      </Link>
    </li>
  );
}
