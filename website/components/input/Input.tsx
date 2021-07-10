import styles from "./Input.module.scss";

import {
  ChangeEventHandler,
  FocusEventHandler,
  MouseEventHandler,
  useState,
} from "react";

interface Props {
  id?: string;
  name?: string;
  type: "text" | "password" | "button";
  onChange?: ChangeEventHandler;
  onClick?: MouseEventHandler;
  onBlur?: FocusEventHandler;
  width?: string;
  placeholder?: string;
  adornment?: React.ReactNode;
  value?: string;
  error?: string;
  warning?: string;
  disabled?: boolean;
}

export default function Input(props: Props) {
  const inputError = () => {
    if (props.error) {
      return (
        <div className={styles.inputError}>
          <p>{props.error}</p>
        </div>
      );
    }
  };

  const inputWarning = () => {
    if (!props.error) {
      if (props.warning) {
        return (
          <div className={styles.inputWarning}>
            <p>{props.warning}</p>
          </div>
        );
      }
    }
  };

  const borderStyle = () => {
    if (props.error) {
      return "rgb(255,120,120)";
    } else if (!props.error && props.warning) {
      return "rgb(255,170,124)";
    } else {
      return "#ccc";
    }
  };

  return (
    <div
      className={styles.customInput}
      style={{ maxWidth: props.width ? props.width : "100%" }}
    >
      <input
        style={{
          border: `1px solid ${borderStyle()}`,
        }}
        id={props.id}
        name={props.name}
        type={props.type}
        placeholder={props.placeholder}
        value={props.value}
        onChange={props.onChange}
        onClick={props.onClick}
        onBlur={props.onBlur}
        disabled={props.disabled}
      />

      {inputError()}
      {inputWarning()}
    </div>
  );
}
