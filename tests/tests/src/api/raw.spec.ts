import { expect, test } from '@playwright/test';
import { testNs, testUser, quidServerUrl, serverUrl } from "../../conf";


test('api', async ({ page, request }) => {
  // request without token
  const issues = await request.get(serverUrl);
  expect(issues.status()).toEqual(401)
  // grab a refresh token
  const resp = await request.post(quidServerUrl + `/token/refresh/24h`, {
    data: {
      namespace: testNs,
      username: testUser.name,
      password: testUser.pwd,
    }
  });
  const rt = await resp.json()
  console.log("Refresh token", rt);
  const refreshToken = rt.token;
  // grab an access token
  const resp2 = await request.post(quidServerUrl + `/token/access/5m`, {
    data: {
      namespace: testNs,
      refresh_token: refreshToken,
    }
  });
  const at = await resp2.json()
  console.log("Access token", at);
  const accessToken = at.token;
  // request with token
  const issues2 = await request.get(serverUrl, {
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': "Bearer " + accessToken
    }
  })
  expect(issues2.status()).toEqual(200)
  await page.pause();
});