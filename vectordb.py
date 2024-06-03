# from qdrant_client import QdrantClient

# # Initialize the client
# client = QdrantClient(":memory:")

# # Prepare your documents, metadata, and IDs
# docs = ["Qdrant has Langchain integrations", "Qdrant also has Llama Index integrations"]
# metadata = [
#     {"source": "Langchain-docs"},
#     {"source": "Linkedin-docs"},
# ]
# ids = [42, 2]

# # Use the new add method
# client.add(
#     collection_name="demo_collection",
#     documents=docs,
#     metadata=metadata,
#     ids=ids
# )

# search_result = client.query(
#     collection_name="demo_collection",
#     query_text="Linkedin"
# )
# print(search_result)