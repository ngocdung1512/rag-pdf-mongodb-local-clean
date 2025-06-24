CÂU LỆNH DÙNG ĐỂ CHẠY: & "C:\Users\ADMIN\anaconda3\envs\mongodb\Scripts\streamlit.exe" run chatbot-app.py


# 🧠 Chat với PDF bằng MongoDB Vector Store

Ứng dụng cho phép người dùng:
- Upload file PDF.
- Trích xuất và xử lý nội dung → embeddings.
- Lưu embeddings vào MongoDB với metadata.
- Đặt câu hỏi và nhận câu trả lời dựa trên PDF đã lưu.

---

## 🔐 1. Cấu hình MongoDB

```python
ATLAS_URI = getenv("ATLAS_URI")
MONGODB_DB = getenv("MONGODB_DB")
MONGODB_COLLECTION = getenv("MONGODB_COLLECTION")
client = MongoClient(ATLAS_URI, server_api=ServerApi('1'))
```

---

## ✅ 2. Kiểm tra kết nối MongoDB

```python
def test_mongodb_connection():
    client.admin.command('ping')
```

---

## 🧠 3. Cấu hình Cache cho LLM

```python
set_llm_cache(MongoDBCache(...))
```

---

## 📄 4. Xử lý PDF

```python
def get_pdf_text(uploaded_files)
def get_text_chunks(text)
```

---

## 🧠 5. Lưu embeddings vào MongoDB

```python
def get_vectorstore(text_chunks, source_name):
    metadatas = [{"source": source_name} for _ in text_chunks]
    vector_search.add_texts([chunk], [metadata])
```

---

## 🔄 6. Tải lại vectorstore (không cần reprocess)

```python
def load_vectorstore():
    return MongoDBAtlasVectorSearch(...)
```

---

## 💬 7. Truy vấn với LLM Chain

```python
def get_conversation_chain(vectorstore):
    retriever = vectorstore.as_retriever(...)
    return ConversationalRetrievalChain(...)
```

---

## 🖥️ 8. Hàm main()

- Upload file
- Process file → vector → lưu MongoDB
- Gọi lại `get_conversation_chain`

---

## ✅ Tổng kết luồng xử lý

| Giai đoạn | Tác vụ |
|----------|--------|
| Upload | Người dùng chọn file PDF |
| Process | Trích xuất → chunk → embed → lưu |
| Query | Hỏi → tìm đoạn phù hợp → trả lời |
| Reuse | Không cần upload lại sau này |

---

