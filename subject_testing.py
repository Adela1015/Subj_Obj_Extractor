import re

def extract_subject(sentence):
    # 使用正則表達式來匹配日語句子的主詞
    # 這裡假設主詞出現在句子的開頭，並且由名詞構成
    pattern = r'(\S+?)が'
    match = re.search(pattern, sentence)
    if match:
        return match.group(1)
    else:
        return None

# 測試程式
test_sentences = [
    "私（わたし）がリンゴを食べます。",
    "彼（かれ）が本を読みます。",
    "私（わたし）が友達を見ます。",
    "彼女（かのじょ）が花を買います。",
    "私（わたし）が犬を飼います。",
    "田中さんが車を運転します。",
    "あなたが手紙を書きます。",
    "先生が生徒に教えます。",
    "子供がお菓子を食べます。",
    "あなたが問題を解決します。",
    "友達がプレゼントを持ってきます。",
    "彼が日本語を話します。",
    "先生が質問に答えます。",
    "私が夕食を作ります。",
    "彼女がピアノを弾きます。",
    "あなたが助けを求めます。",
    "子供が遊びます。",
    "先生が新しい言葉を教えます。",
    "私がお茶を飲みます。",
    "彼がボールを投げます。"
]

for sentence in test_sentences:
    subject = extract_subject(sentence)
    if subject:
        print(f"句子 '{sentence}' 的主詞是：{subject}")
    else:
        print(f"找不到句子 '{sentence}' 的主詞。")