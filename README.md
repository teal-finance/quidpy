# Quidpy

A requests library for the Quid json web tokens server

## TODO

Add support for signing verification for the following algorithms:

- HS256 = HMAC using SHA-256
- HS384 = HMAC using SHA-384
- HS512 = HMAC using SHA-512
- RS256 = RSASSA-PKCS1-v1_5 using 2048-bits RSA key and SHA-256
- RS384 = RSASSA-PKCS1-v1_5 using 2048-bits RSA key and SHA-384
- RS512 = RSASSA-PKCS1-v1_5 using 2048-bits RSA key and SHA-512
- ES256 = ECDSA using P-256 and SHA-256
- ES384 = ECDSA using P-384 and SHA-384
- ES512 = ECDSA using P-521 and SHA-512
- EdDSA = Ed25519

## Unit tests

Create a test namespace in a Quid instance and create a user. Open `tests/src/conf.ts` and
update the namespace key and credentials. Then run the test server:

```
pip install pytest
cd example
export QUID_DEMO_KEY=key_of_the_testns_namespace
export FLASK_APP=server.py
flask run
```

Then run the tests:

```
pytest
```