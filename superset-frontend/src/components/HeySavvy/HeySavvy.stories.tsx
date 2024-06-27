import type { Meta, StoryObj } from '@storybook/react';

import { HeySavvy } from './HeySavvy';

const meta: Meta<typeof HeySavvy> = {
  component: HeySavvy,
};

export default meta;

type Story = StoryObj<typeof HeySavvy>;

export const Basic: Story = { args: {} };
