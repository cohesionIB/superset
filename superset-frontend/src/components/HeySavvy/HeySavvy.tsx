import React, { useEffect, useRef, useState } from 'react';
import { Button, Drawer, Modal } from 'antd';
import './heySavvy.css';
import Icon, {
  CustomIconComponentProps,
} from '@ant-design/icons/lib/components/Icon';
import HeySavvySvg from '../../assets/images/icons/hey_savvy.svg';

const HeySavvyIcon = (props: Partial<CustomIconComponentProps>) => (
  <Icon component={HeySavvySvg} {...props} />
);

export function HeySavvy() {
  const heySavvyHostURL: string = process.env.REACT_APP_HEY_SAVVY_HOST ?? '';

  const [open, setOpen] = useState(false);
  const showDrawer = () => {
    setOpen(true);
  };

  const onClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Button
        type="primary"
        icon={<HeySavvyIcon />}
        className="hey-savvy-btn"
        onClick={showDrawer}
      >
        Hey Savvy!
      </Button>

      <Drawer onClose={onClose} visible={open} width={400}>
        <iframe
          title="Hey Savvy Assistant"
          src={heySavvyHostURL}
          height="100%"
          width="100%"
        />
      </Drawer>
    </div>
  );
}
