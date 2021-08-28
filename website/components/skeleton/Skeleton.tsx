import styles from "./Skeleton.module.scss";

interface Props {
  type: string;
  width?: string;
  height?: string;
  boxShadow?: string;
  onClick?: React.MouseEventHandler;
}

export default function Skeleton(props: Props) {
  const { type, width, height, boxShadow } = props;

  return (
    <div
      className={`${styles.skeleton} ${type == "circle" && styles.circle}`}
      style={{
        width: width ? width : "100%",
        height: height ? height : width ? width : "200px",
        boxShadow: boxShadow ? boxShadow : "0 0 5px 1px rgb(129, 129, 129, 0.3)"
      }}
    />
  );
}
