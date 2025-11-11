the project i made for chapters up until 3, mainly follows clean code rules, however there are some notes:

## database/db.py mixes database operations with CRUD, better to split into more modules.

this is chatgpt's overview of my code : 

| Principle                    | Status | Notes                              |
| ---------------------------- | ------ | ---------------------------------- |
| **Meaningful Names**         | ✅      | Good descriptive names overall     |
| **Single Responsibility**    | ⚠️     | Mixes connection + logic           |
| **Avoid Duplication**        | ⚠️     | Repeated patterns across endpoints |
| **Error Handling**           | ⚠️     | Needs explicit try/except          |
| **Environment Isolation**    | ⚠️     | Hardcoded DB URL                   |
| **Layered Architecture**     | ⚠️     | Mixes API & data logic             |
| **Small, Focused Functions** | ✅      | Most functions are concise         |

so overall we are on the right track, now i will move on to fixing this project.

also `having .env file is a must`.