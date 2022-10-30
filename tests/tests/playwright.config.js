const { devices } = require('@playwright/test');/** @type {import('@playwright/test').PlaywrightTestConfig} */
const config = {
  workers: 1,
  retries: 1,
  use: {
    headless: true,
    viewport: { width: 1280, height: 720 },
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'safari',
      use: { ...devices['iPhone 12'] },
    },
  ],
};

module.exports = config;