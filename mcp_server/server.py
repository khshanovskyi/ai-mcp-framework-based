from pathlib import Path

from mcp.server.fastmcp import FastMCP

from mcp_server.models.user_info import UserSearchRequest, UserCreate, UserUpdate
from mcp_server.user_client import UserClient

#TODO:
# 1. Create instance of FastMCP as `mcp` (or another name if you wish) with:
#       - name is "users-management-mcp-server",
#       - host is "0.0.0.0",
#       - port is 8005,
# 2. Create UserClient


# ==================== TOOLS ====================
#TODO:
# You need to add all the tools here. You will need to create 5 async methods and mark them as @mcp.tool() (if you
# named FastMCP not as `mcp` then use the name that you have used). All tools return `str`.
# Don't forget about tool description, it will LLM to identify when some particular tool should be used.
# https://gofastmcp.com/servers/tools
# ---
# Tools:
# 1. `get_user_id`:-
# 2. `delete_user`:-
# 3. `search_user`:-
# 4. `add_user`:-
# 5. `update_user`:-

# ==================== MCP RESOURCES ====================

#TODO:
# Provides screenshot with Swagger endpoints of User Service. We need for the case to show you that MCP servers can
# provide some static resources.
# https://gofastmcp.com/servers/resources
# ---
# 1. Create async method `get_flow_diagram` that returns bytes and mark as `@mcp.resource` with:
#   - uri = "users-management://flow-diagram"
#   - mime_type="image/png"
# 2. You need to get `flow.png` picture from `mcp_server` folder and return it as bytes.
# 3. Don't forget to provide resource description


# ==================== MCP PROMPTS ====================

#TODO:
# Provides static prompts that can be used by Clients
# https://gofastmcp.com/servers/prompts
# ---
# Prompts are prepared, you need just properly return them and provide descriptions of them"

# Helps users formulate effective search queries
"""
You are helping users search through a dynamic user database. The database contains 
realistic synthetic user profiles with the following searchable fields:

## Available Search Parameters
- **name**: First name (partial matching, case-insensitive)
- **surname**: Last name (partial matching, case-insensitive)  
- **email**: Email address (partial matching, case-insensitive)
- **gender**: Exact match (male, female, other, prefer_not_to_say)

## Search Strategy Guidance

### For Name Searches
- Use partial names: "john" finds John, Johnny, Johnson, etc.
- Try common variations: "mike" vs "michael", "liz" vs "elizabeth"
- Consider cultural name variations

### For Email Searches  
- Search by domain: "gmail" for all Gmail users
- Search by name patterns: "john" for emails containing john
- Use company names to find business emails

### For Demographic Analysis
- Combine gender with other criteria for targeted searches
- Use broad searches first, then narrow down

### Effective Search Combinations
- Name + Gender: Find specific demographic segments
- Email domain + Surname: Find business contacts
- Partial names: Cast wider nets for common names

## Example Search Patterns
```
"Find all Johns" → name="john"
"Gmail users named Smith" → email="gmail" + surname="smith"  
"Female users with company emails" → gender="female" + email="company"
"Users with Johnson surname" → surname="johnson"
```

## Tips for Better Results
1. Start broad, then narrow down
2. Try variations of names (John vs Johnny)
3. Use partial matches creatively
4. Combine multiple criteria for precision
5. Remember searches are case-insensitive

When helping users search, suggest multiple search strategies and explain 
why certain approaches might be more effective for their goals.
"""


# Guides creation of realistic user profiles
"""
You are helping create realistic user profiles for the system. Follow these guidelines 
to ensure data consistency and realism.

## Required Fields
- **name**: 2-50 characters, letters only, culturally appropriate
- **surname**: 2-50 characters, letters only  
- **email**: Valid format, must be unique in system
- **about_me**: Rich, realistic biography (see guidelines below)

## Optional Fields Best Practices
- **phone**: Use E.164 format (+1234567890) when possible
- **date_of_birth**: YYYY-MM-DD format, realistic ages (18-80)
- **gender**: Use standard values (male, female, other, prefer_not_to_say)
- **company**: Real-sounding company names
- **salary**: $30,000-$200,000 range for employed individuals

## Address Guidelines
Provide complete, realistic addresses:
- **country**: Full country names
- **city**: Actual city names  
- **street**: Realistic street addresses
- **flat_house**: Apartment/unit format (Apt 123, Unit 5B, Suite 200)

## Credit Card Guidelines  
Generate realistic but non-functional card data:
- **num**: 16 digits formatted as XXXX-XXXX-XXXX-XXXX
- **cvv**: 3 digits (000-999)
- **exp_date**: MM/YYYY format, future dates only

## Biography Creation ("about_me")
Create engaging, realistic biographies that include:

### Personality Elements
- 1-3 personality traits (curious, adventurous, analytical, etc.)
- Authentic voice and writing style
- Cultural and demographic appropriateness

### Interests & Hobbies  
- 2-4 specific hobbies or activities
- 1-3 broader interests or passion areas
- 1-2 life goals or aspirations

### Biography Templates
Use varied narrative structures:
- "I'm a [trait] person who loves [hobbies]..."
- "When I'm not working, you can find me [activity]..."  
- "Life is all about balance for me. I enjoy [interests]..."
- "As someone who's [trait], I find great joy in [hobby]..."

## Data Validation Reminders
- Email uniqueness is enforced (check existing users)
- Phone numbers should follow consistent formatting
- Date formats must be exact (YYYY-MM-DD)
- Credit card expiration dates must be in the future
- Salary values should be realistic for the demographic

## Cultural Sensitivity
- Match names to appropriate cultural backgrounds
- Consider regional variations in address formats
- Use realistic company names for the user's location
- Ensure hobbies and interests are culturally appropriate

When creating profiles, aim for diversity in:
- Geographic representation
- Age distribution  
- Interest variety
- Socioeconomic backgrounds
- Cultural backgrounds
"""


if __name__ == "__main__":
    #TODO:
    # Run server with `transport="streamable-http"`
    raise NotImplementedError()
