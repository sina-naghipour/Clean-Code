### original function

```python
async def createUser(email: str, password: str):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User).where(User.email == email))
        existing_user = result.scalars().first()
        if existing_user:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail      = 'Email already registered.'
            )
            
        user = User(email=email, password_hash=hashPassword(password))
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
```

### Clean code version of the function

```python
async def createUser(email: str, password: str):
    async with AsyncSessionLocal() as session:
        userExistenceResult = await session.execute(select(User).where(User.email == email))
        existingUser = userExistenceResult.scalars().first()
        if existingUser:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail      = 'Email already registered.'
            )
            
        createdUser = User(email=email, password_hash=hashPassword(password))
        session.add(createdUser)
        await session.commit()
        await session.refresh(createdUser)
        return createdUser
```

i have turned my previous function to this, with the help of ai, i have learned that converting `result` to `userExistenceResult` is over doing clean code, it could just be result.

also, pythonic way to name things is not camel case, it is the usage of `underscore`.


### Original Function

```python
def create_access_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

```


### Clean code version of the function

```python
def create_access_token(subject: str) -> str:
    created_token_expire_datetime = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    created_token_payload = {"sub": subject, "exp": created_token_expire_datetime}
    return jwt.encode(created_token_payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

```

converting `exprie` and `payload` is not okay, they work just fineeee.

maybe `expire_time` is better, but no need to change `payload`.
