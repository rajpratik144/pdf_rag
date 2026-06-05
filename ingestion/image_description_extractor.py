# ==========================================
# File: ingestion/image_description_extractor.py
# ==========================================

from pathlib import Path
from langchain_core.documents import (Document)
from langchain_google_genai import (ChatGoogleGenerativeAI)
from langchain_core.messages import (HumanMessage)
from ingestion.image_extractor import (ImageExtractor)
from ingestion.page_renderer import (PageRenderer)
import os
import base64

class ImageDescriptionExtractor:
    @staticmethod
    def extract(pdf_path):

        llm = (ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=os.getenv("GOOGLE_API_KEY"),temperature=0))

        image_documents = []

        images = (ImageExtractor.extract(pdf_path))

        for image in images:
            page = (image["page"])

            image_path = (PageRenderer.render_page(pdf_path=pdf_path,page_number=page))
            with open(image_path,"rb") as file:
                image_base64 = (base64.b64encode(file.read()).decode("utf-8"))
            message = (
                HumanMessage(
                    content=[
                        {
                            "type":"text",
                            "text":"""
                                        You are generating semantic descriptions for a document retrieval system.

                                        Describe the image in a concise way that preserves information useful for answering future questions.

                                        If the image is:
                                        - a chart, explain the trend.
                                        - a graph, explain the data.
                                        - a table image, summarize it.
                                        - a diagram, explain its components.
                                        - a product or advertisement, summarize the important details.

                                        Do not mention colors or visual styling unless they are important.
                                        Return one concise paragraph.
                                    """
                        },
                        {
                            "type":"image_url",
                            "image_url":f"data:image/png;base64,{image_base64}"
                        }
                    ]
                )
            )

            response = (llm.invoke([message]))
            image_documents.append(
                Document(
                    page_content=
                    "IMAGE DESCRIPTION\n\n" + response.content,
                    metadata={
                        "page":page,
                        "type":"image"
                    }
                )
            )
        return (image_documents)