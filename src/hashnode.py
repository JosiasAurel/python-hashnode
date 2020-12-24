

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
        self.client = client = Client(
            transport=TRANSPORT, fetch_schema_from_transport=True)

    # the below are queries

    def get_user_info(self, username: str):
        query = gql(""" 
            Query User(username: {0}) {
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
         """.format(username))
        res = self.client.execute(query)
        return res

    def get_feed(self, feed_type: str, page=0):
        # accepted feed type :
        # BEST
        # FEATURED
        # NEW
        # COMMUNITY
        query = gql(""" 
            query StoriesFeed(type: {0}, page: {1}) {
                _id,
                title,
                author,
                tags,
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
         """.format(feed_type, page))

        res = self.client.execute(query)
        return res

    def get_amas(self, page=0):
        query = gql(
            """ 
                query amas({0}) {
                    _id,
                title,
                author,
                tags,
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
             """.format(page)
        )

        res = self.client.execute(query)
        return res

    def get_post(self, slug: str, hostname: str):
        query = gql(
            """ 
                query post({0}, {1}) {
                    _id, 
                    cuid,
                    slug,
                    title,
                    type,
                    author,
                    dateAdded,
                    tags,
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
             """.format(slug, hostname)
        )

        res = self.client.execute(query)
        return res

    def get_tag_categories(self):
        query = gql(
            """ 
            query tagCategories {
                _id,
                name,
                isActive,
                priority,
                slug,
                tags
            }
             """
        )

        result = self.client.execute(query)
        return result

    # here marks the end of queries and the beginning of mutations

    def follow_user(self, user_id: str):
        mutation = gql(
            """ 
                mutation followUser(userId{0}) {
                    code,
                    success,
                    message
                }
             """.format(user_id)
        )

        result = self.client.execute(mutation)
        return result

    def create_story(self, story: str):
        mutation = gql(
            """ 
                mutation createStory(input: {0}) {
                    code,
                    success,
                    message,
                    post
                }
             """.format(story)
        )

        result = self.client.execute(mutation)
        return result

    def create_publication_story(self, story_input: str, publication_id: str, hide_from_hashnode_feed: bool = False):
        mutation = gql(
            """ 
                mutation createPublicationStory(input: {0}, publicationId: {1}, hideFromHashnodeFeed:{2}) {
                    code,
                    success,
                    message,
                    post
                }
             """.format(story_input, publication_id, hide_from_hashnode_feed)
        )

        result = self.client.execute(mutation)

        return result

    def update_story(self, post_id: str, story: str):
        mutation = gql(
            """ 
                mutation updateStory(postId:{0}, input:{1}) {
                    code,
                    success,
                    message,
                    post
                }
             """.format(post_id, story)
        )

        result = self.client.execute(mutation)

        return result

    def react_to_story(self, reaction):
        mutation = gql(
            """ 
                mutation reactToStory(input:{0}) {
                    code,
                    success,
                    message
                }
             """.format(reaction)
        )

        result = self.client.execute(mutation)

        return result

    def delete_post(self, post_id: str):
        mutation = gql(
            """ 
                mutation deletePost(id:{0}) {
                    code,
                    success,
                    message
                }
             """.format(post_id)
        )

        result = self.client.execute(mutation)

        return result

    def create_response(self, response: str):
        mutation = gql(
            """ 
                mutation createResponse(input:{0}) {
                    code,
                    success,
                    message,
                    response
                }
             """.format(response)
        )

        result = self.client.execute(mutation)

        return result

    def update_reponse(self, response_id: str, post_id: str, content: str):
        mutation = gql(
            """ 
                mutation updateResponse(responseId:{0}, postId:{1}, contentInMarkdown:{2}) {
                    code,
                    success,
                    message,
                    response
                }
             """.format(response_id, post_id, content)
        )

        result = self.client.execute(mutation)

        return result

    def react_to_response(self, response: str):
        mutation = gql(
            """ 
                mutation reactToResponse(input: {0}) {
                    code,
                    success,
                    message
                }
             """.format(response)
        )

        result = self.client.execute(mutation)

        return result

    def delete_response(self, response_id: str, post_id: str):
        mutation = gql(
            """ 
                mutation deleteResponse(responseId:{0}, postId:{1}) {
                    code,
                    success,
                    message
                }
             """.format(response_id, post_id)
        )

        result = self.client.execute(mutation)

        return result

    def create_reply(self, reply: str):
        mutation = gql(
            """ 
                mutation createReply(input:{0}) {
                    code,
                    success,
                    message,
                    reply
                }
             """.format(reply)
        )

    def update_reply(self, reply_id: str, response_id: str, post_id: str, new_reply: str):
        mutation = gql(
            """ 
                mutation updateReply(replyId:{0}, responseId:{1}, postId{2}, contentInMarkdown:{3}) {
                    code,
                    success,
                    message,
                    reply
                }
             """.format(reply_id, response_id, post_id, new_reply)
        )

        result = self.client.execute(mutation)

        return result

    def react_to_reply(self, reply: str):
        mutation = gql(
            """ 
                mutation reactToReply(input:{0}) {
                    code,
                    success,
                    message,
                    reply
                }
             """.format(reply)
        )

        result = self.client.execute(mutation)

        return result

    def delete_reply(self, reply_id: str, response_id: str, post_id: str):
        mutation = gql(
            """ 
                mutation deleteReply(replyId:{0}, responseId:{1}, postId:{2}) {
                    code,
                    success,
                    message
                }
             """.format(reply_id, response_id, post_id)
        )


""" 
Executong results with the gql
result = client.execute(query:str)

"""
