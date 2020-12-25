

"""
This is a lightweight wrapper around the hashnode GraphQL API implemented in Python

Author : Josias Aurel
Author_website : josiasaurel.tech
Website : hashnode.josiasaurel.tech
This is open source
contributions are all welcome. Just send a pull request

"""


from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


class Hashnode(object):
    def __init__(self, api_token: str):
        self.api_token = api_token
        TRANSPORT = AIOHTTPTransport(
            url="https://api.hashnode.com/", headers={"Authorization": api_token})

        # create graphql client to interact with the hashnode api
        client = Client(
            transport=TRANSPORT, fetch_schema_from_transport=True)
        self.client = client  # set the class client as the hashnode graphql api client

    # the below are queries

    def get_user_info(self, username: str):
        query = gql("""
            query($username: String!) {
                user(username: $username) {
                _id,
                name,
                username,
                blogHandle,
                followers,
                publicationDomain,
                tagline,
                isEvangelist,
                dateJoined,
                socialMedia,
                numFollowing,
                numFollowers,
                coverImage,
                location,
                photo,
                numPosts,
                numReactions,
                publication
            }
            }
         """)
        params = {
            "username": username
        }
        res = self.client.execute(query, variable_values=params)
        return res

    def get_feed(self, feed_type: str, page=0):
        # accepted feed type :
        # BEST
        # FEATURED
        # NEW
        # COMMUNITY
        query = gql("""
            query($type:FeedType!, $page: Int) {
                storiesFeed(type: $type, page: $page) {
                _id,
                title,
                author {
                    name,
                    username,
                    blogHandle,
                    photo
                },
                tags {
                    name,
                    logo,
                    slug,
                    wiki,
                    managers {
                        role,
                        user { name, blogHandle
                      }
                    }
                },
                slug,
                cuid,
                type,
                coverImage,
                brief,
                dateUpdated,
                followersCount,
                popularity,
                totalReaction,
                dateAdded,
                responseCount,
                dateFeatured,
                responseCount,
                reactionsByCurrentUser,
                bookMarkedIn,
                isAnonymous,
                poll,
                replyCount,
                contentMarkdown
            }
            }
         """)

        params = {
            "type": feed_type,
            "page": page
        }

        res = self.client.execute(query, variable_values=params)
        return res

    def get_amas(self, page=0):
        query = gql(
            """
                query($page: Int) {
                    amas(page: $page) {
                    _id,
                title,
                author {
                    name,
                    username,
                    blogHandle,
                    photo
                },
                tags {
                    name,
                    logo,
                    slug,
                    wiki,
                                            managers {
                                                role,
                                                user {
                                                 name, blogHandle
                                            }
                },
                slug,
                cuid,
                type,
                coverImage,
                brief,
                dateUpdated,
                followersCount,
                popularity,
                totalReaction,
                dateAdded,
                responseCount,
                dateFeatured,
                responseCount,
                reactionsByCurrentUser,
                bookMarkedIn,
                isAnonymous,
                poll,
                replyCount,
                contentMarkdown
                }
                }
             """
        )

        params = {
            "page": page
        }
        res = self.client.execute(query, variable_values=params)
        return res

    def get_post(self, slug: str, hostname: str):
        query = gql(
            """
                query($slug: String!, $hostname: String) {
                    post(slug: $slug, hostname:$hostname) {
                    _id,
                    cuid,
                    slug,
                    title,
                    type,
                    author {
                    name,
                    username,
                    blogHandle,
                    photo
                },
                    dateAdded,
                    tags {
                    name,
                    logo,
                    slug,
                    wiki,
                                            managers {
                        role,
                        user {name, blogHandle}
                    }
                },
                    contributors,
                    coverImage,
                    brief,
                    dateUpdated,
                    isFeatured,
                    reactions,
                    replyCount,
                    responseCount,
                    sourceFromGithub,
                    isRepublished,
                    followersCount,
                    untaggedFrom,
                    reactionsByCurrentUser,
                    poll,
                    popularity,
                    content,
                    contentMarkdown

                }
                }
             """
        )
        params = {
            "slug": slug,
            "hostname": hostname
        }
        res = self.client.execute(query, variable_values=params)
        return res

    def get_tag_categories(self):
        query = gql(
            """
            {
                tagCategories {
                _id,
                name,
                isActive,
                priority,
                slug,
                tags {
                    name,
                    logo,
                    slug,
                    wiki,
                            managers {role, user{name, blogHandle}}
                }
            }
            }
             """
        )

        result = self.client.execute(query)
        return result

    # here marks the end of queries and the beginning of mutations

    def follow_user(self, user_id: str):
        mutation = gql(
            """
                mutation($userId: String!) {
                    followUser(userId: $userId) {
                    code,
                    success,
                    message
                }
                }
             """
        )
        params = {
            "userId": user_id
        }
        result = self.client.execute(mutation, variable_values=params)
        return result

    def create_story(self, story: str):
        mutation = gql(
            """
                mutation($input: CreateStoryInput!) {
                    createStory(input:$input) {
                    code,
                    success,
                    message,
                    post
                }
                }
             """
        )
        params = {
            "input": story
        }
        result = self.client.execute(mutation, variable_values=params)
        return result

    def create_publication_story(self, story_input: str, publication_id: str, hide_from_hashnode_feed: bool = False):
        mutation = gql(
            """
                mutation($input: CreateStoryInput!, publicationId: String!, $hideFromHashnodeFeed: Boolean) {
                    createPublicationStory(input: $input, publicationId: $publicationId, hideFromHashnodeFeed:$hideFromHashnodeFeed) {
                    code,
                    success,
                    message,
                    post
                }
                }
             """
        )
        params = {
            "input": story_input,
            "publicationId": publication_id,
            "hideFromHashnodeFeed": hide_from_hashnode_feed
        }
        result = self.client.execute(mutation, variable_values=params)

        return result

    def update_story(self, post_id: str, story: str):
        mutation = gql(
            """
                mutation($postId: String!, $input: UpdateStoryInput!) {
                    updateStory(postId:$postId, input:$input) {
                    code,
                    success,
                    message,
                    post
                }
                }
             """)
        params = {
            "postId": post_id,
            "input": story
        }

        result = self.client.execute(mutation, variable_values=params)

        return result

    def react_to_story(self, reaction):
        mutation = gql(
            """
                mutation($input: ReactToPostInput!) {
                    reactToStory(input:$input) {
                    code,
                    success,
                    message
                }
                }
             """
        )
        params = {
            "input": reaction
        }
        result = self.client.execute(mutation, variable_values=params)

        return result

    def delete_post(self, post_id: str):
        mutation = gql(
            """
                mutation($id: String!) {
                    deletePost(id:$id) {
                    code,
                    success,
                    message
                }
                }
             """
        )
        params = {
            "id": post_id
        }
        result = self.client.execute(mutation, variable_values=params)

        return result

    def create_response(self, response: str):
        mutation = gql(
            """
                mutation($input: CreateResponseInput!) {
                    createResponse(input:$input) {
                    code,
                    success,
                    message,
                    response
                }
                }
             """
        )
        params = {
            "input": response
        }
        result = self.client.execute(mutation, variable_values=params)

        return result

    def update_reponse(self, response_id: str, post_id: str, content: str):
        mutation = gql(
            """
                mutation($responseId: String!, $postId: String, $contentInMarkdown: String!) {
                    updateResponse(responseId:$responseId, postId:$postId, contentInMarkdown:$contentInMarkdown) {
                    code,
                    success,
                    message,
                    response
                }
                }
             """
        )
        params = {
            "responseId": response_id,
            "postId": post_id,
            "contentInMarkdown": content
        }
        result = self.client.execute(mutation, variable_values=params)

        return result

    def react_to_response(self, response: str):
        mutation = gql(
            """
                mutation($input: ReactToResponseInput!) {
                    reactToResponse(input: $input) {
                    code,
                    success,
                    message
                }
                }
             """)

        params = {
            "input": response
        }

        result = self.client.execute(mutation, variable_values=params)

        return result

    def delete_response(self, response_id: str, post_id: str):
        mutation = gql(
            """
                mutation($responseId: String!, $postId: String!) {
                    deleteResponse(responseId:$responseId, postId:$postId) {
                    code,
                    success,
                    message
                }
                }
             """
        )
        params = {
            "responseId": response_id,
            "postId": post_id
        }
        result = self.client.execute(mutation, variable_values=params)

        return result

    def create_reply(self, reply: str):
        mutation = gql(
            """
                mutation($input: CreateReplyInput!) {
                    createReply(input: $input) {
                    code,
                    success,
                    message,
                    reply
                    }
                }
             """
        )

        params = {
            "input": reply
        }

        result = self.client.execute(mutation, variable_values=params)

        return result

    def update_reply(self, reply_id: str, response_id: str, post_id: str, new_reply: str):
        mutation = gql(
            """
                mutation($replyId: String!, $responseId: String!, $postId: String!, $contentInMarkdown: String!) {
                    updateReply(replyId:$replyId, responseId:$responseId, postId:$postId, contentInMarkdown:$contentInMarkdown) {
                    code,
                    success,
                    message,
                    reply
                }
                }
             """
        )
        params = {
            "replyId": reply_id,
            "responseId": response_id,
            "postId": post_id,
            "contentInMarkdown": new_reply
        }
        result = self.client.execute(mutation, variable_values=params)

        return result

    def react_to_reply(self, reply: str):
        mutation = gql(
            """
                mutation($input: ReactToReplyInput!) {
                    reactToReply(input:$input) {
                    code,
                    success,
                    message,
                    reply
                }
                }
             """
        )
        params = {
            "input": reply
        }
        result = self.client.execute(mutation, variable_values=params)

        return result

    def delete_reply(self, reply_id: str, response_id: str, post_id: str):
        mutation = gql(
            """
                mutation($replyId: String!, $responseId: String!, $postId: String!) {
                    deleteReply(replyId:$replyId, responseId:$responseId, postId:$postId) {
                    code,
                    success,
                    message
                }
                }
             """
        )

        params = {
            "replyId": reply_id,
            "responseId": response_id,
            "postId": post_id
        }

        result = self.client.execute(mutation, variable_values=params)

        return result


"""
Executong results with the gql
result = client.execute(query:str)

"""
