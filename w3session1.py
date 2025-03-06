"""
Problem 1: Post Format Validator
You are managing a social media platform and need to ensure that posts are properly formatted. 
Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. 
You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.
def is_valid_post_format(posts):
  pass
Example Usage:

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
Example Output:

True
True
False

"""

def is_valid_post_format(posts):
  #understand
  # match corresponding tags
  #true if they are, false if they are not

  #match
  #stack

  #plan

  
    # if posts is empty: return False
   if not posts: 
        return False
    #stack
   stack = []
    # loop over the posts
   tags = {"]": "[", ")":"(", "}": "{"}
   for tag in posts:
       
    #   if current tag is open: push that into a stack
    if tag == "(" or tag == "[" or tag == "{":
       stack.append(tag)
    # if stack is not empty and if its a matching close tag: then you pop
    elif len(stack) != 0 and tags[tag] == stack[-1] :
       stack.pop()

   print(stack)
    # return if stack is empty
   return len(stack) == 0


print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))