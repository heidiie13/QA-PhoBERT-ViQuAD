from transformers import pipeline

def init_model(model_name="heidiie/phobert_finetuned_viquad"):
    print("Init pipeline ...")
    return pipeline("question-answering", model=model_name)

_qa_pipeline = init_model()

def get_answer(question: str, context: str):
    answer = _qa_pipeline(question=question, context=context)
    return answer['answer']