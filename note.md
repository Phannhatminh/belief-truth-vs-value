# Hai chữ "belief" — LLM có phân biệt được không? — ghi chú dự án

## 0. Đề bài (chốt 2026-09-27)

> **Khi chữ "believe" giống hệt nhau và chỉ có ngữ cảnh quyết định nó là niềm tin *truth-seeking* hay niềm tin *vì giá trị*, LLM có phân biệt được hai cách đọc đó không?**

Các phần bên dưới (tài liệu belief / acceptance / belief-in, novelty, Steele et al.) được viết **trước khi** chốt đề bài. Chúng vẫn là nền tham khảo, nhưng đề bài chỉ có **hai** cách đọc dưới đây. Belief-in (Audi) nằm ngoài phạm vi.

## 1. Hai cách đọc

| | **Truth-seeking** | **Vì giá trị** |
|---|---|---|
| Hướng tới | Đúng với thế giới | Kết cục tốt hơn nhờ chính việc tin |
| Quan hệ với bằng chứng | Đi theo bằng chứng; credence cao | Có thể đi ngược bằng chứng; **credence thấp vẫn giữ nguyên** |
| Được chọn tự nguyện? | Không | Có (một lựa chọn thái độ) |
| Tính hợp lý | Hợp lý về nhận thức | Hợp lý về thực tiễn |
| Gần với trong văn liệu | Belief proper (Cohen, Engel) | Acceptance vì mục đích (Cohen); non-epistemic belief (Vesga, Van Leeuwen & Lombrozo 2025); *The Will to Believe* (James); Pascal |

### Ví dụ minh họa (của người đề xuất)
Bệnh nhân ung thư, P(phẫu thuật thành công) = 0.1.
- P(sống | thành công, tin) = 0.6; P(sống | thành công, không tin) = 0.2; P(sống | thất bại) ≈ 0.
- Tin: 0.1 × 0.6 = **0.06**. Không tin: 0.1 × 0.2 = **0.02**.
- Credence vẫn là 0.1 (không tự lừa mình). Thứ được chọn là **thái độ**, và thái độ là một biến nhân quả trong kết cục. Vì vậy "tin" ở đây hợp lý trong khung quyết định của người đó.

Ghi chú khi formalize:
- Với các con số này, tin trội hơn với mọi P(s) > 0. Muốn có ngưỡng thì cần thêm **chi phí của việc tin**: `tin ⇔ P(s)·[P(sống|s,tin) − P(sống|s,¬tin)]·U(sống) > chi phí(tin)`.
- Có hai cơ chế con:
  - (a) niềm tin *thay đổi xác suất kết cục* (phẫu thuật, tự hiện thực hóa);
  - (b) niềm tin *giữ người ta ở lại cuộc chơi* (đánh cược), tức là giữ quyền chọn chứ không đổi xác suất.

## 2. "Phân biệt được" nghĩa là gì — ba mức

| Mức | Câu hỏi | Cách đo |
|---|---|---|
| **1. Hành vi** | Mô hình suy luận khác nhau theo cách đọc? | Xác suất các câu nối chẩn đoán: "…so she thinks the odds are good" (truth-seeking) vs "…even though she knows the odds are 10%" (vì giá trị). |
| **2. Biểu diễn** | Hai cách đọc tách được trong activation? | Probe tại token "believes" / mệnh đề p. Phải vượt baseline từ vựng của ngữ cảnh và tổng quát hóa sang miền ngữ cảnh chưa gặp. |
| **3. Nhân quả** | Mô hình *dùng* sự phân biệt đó? | Patching / DAS: ghép biểu diễn từ ngữ cảnh loại A sang loại B, xem suy luận phía sau có đổi theo không. |

Mô hình có thể đạt mức 1 mà không đạt mức 2–3 (chỉ bắt tín hiệu bề mặt). Khoảng chênh giữa các mức là kết quả đáng báo cáo.

## 3. Thiết kế tối thiểu

- **Câu đích giữ nguyên từng chữ**, ví dụ "She believes the surgery will succeed."
- **Ngữ cảnh phía trước chia làm hai loại:**
  - *Truth-seeking*: bằng chứng tốt, xác suất cao được nêu; niềm tin đi theo bằng chứng.
  - *Vì giá trị*: xác suất thấp được nêu rõ + một lợi ích phụ thuộc vào việc tin.
- **Tiêu chí gán nhãn vận hành** cho cách đọc vì giá trị: credence thấp được nêu rõ + lợi ích thực tiễn phụ thuộc vào thái độ + câu *believes that p*.
- **Nhiều miền:** y tế, đánh cược, thể thao, kinh doanh, quan hệ… Train trên một số miền, test trên miền còn lại.
- **Nhãn từ người đánh giá**, dạng liên tục. Mức đồng thuận giữa người với người là mức trần.
- **Kiểm soát tín hiệu bề mặt:** cân bằng từ vựng giữa hai điều kiện; baseline bag-of-words chỉ trên ngữ cảnh.
- **Hai nguồn mẫu:** minimal pair (cho can thiệp nhân quả) + các cách dùng *believe* tự nhiên (để kiểm tra kết quả ngoài phòng thí nghiệm).
- **Pre-register** tiêu chí nhãn, cách chọn mẫu và ngưỡng trước khi chạy mô hình.
- **Nối với Steele et al.:** tương tự hai giá trị belief / reality của họ, ở đây có hai thứ cùng tồn tại là **credence (0.1)** và **thái độ tin (sẽ thành công)**. Câu hỏi: mô hình giữ cả hai, hay gộp lại thành "tin thì chắc xác suất cao"? Gộp lại chính là cách hiểu belief = xác suất duy nhất.

## 4. Abstract (viết lại theo đề bài)

> Large language models are increasingly analyzed as systems that represent attitudes such as belief, yet the English verb *believe* covers at least two distinct attitudes. In its truth-seeking use, believing that *p* tracks evidence about whether *p* is true. In its value-driven use, an agent can believe that *p* while acknowledging that *p* is unlikely, because holding the belief itself improves their prospects — as when a patient facing a 10% chance of surgical success believes the operation will succeed. The second use is not irrational: it is practically rational given the agent's decision problem, even while their credence stays low. The two uses share a single surface form, and which one is meant is typically fixed by context rather than by the sentence. We ask whether language models distinguish them. Holding the belief report fixed word for word and varying only the preceding context, we test at three levels: whether model behavior differs across the two readings, whether the readings are linearly separable in internal representations beyond surface lexical cues and across held-out domains, and whether the distinction is causally used, via activation patching and distributed alignment search on [models]. We further ask whether models maintain the agent's low credence and their value-driven belief as separate representations, or collapse them into a single probabilistic notion of belief. [Key finding.] The study offers a controlled test of whether a context-dependent distinction in attitude, formalized in decision-theoretic terms, emerges in language model representations.

Placeholder cần điền: `[models]`, `[Key finding.]`.

---

# Phụ lục: bản ghi trước khi chốt đề bài

## A1. (Bản cũ) Ý tưởng ban đầu

Từ *belief* / *believe* trong tiếng Anh không gọi tên một thái độ mệnh đề duy nhất. Cùng một biểu thức ngôn ngữ có thể biểu hiện nhiều quan hệ khác nhau giữa chủ thể và đối tượng. Dự án:

1. Xây một ngôn ngữ ngữ nghĩa hình thức biểu diễn các quan hệ này như những thứ riêng biệt, nhưng vẫn giữ hình thức bề mặt chung.
2. Ánh xạ các biểu diễn hình thức lên biểu diễn nội tại của LLM.
3. Dùng mechanistic interpretability để kiểm tra xem các phân biệt đó có được biểu diễn trong mô hình không, có tách được về mặt nhân quả không, và có khôi phục được theo lối kết hợp (compositional) không.

## A2. (Bản cũ) Không gian ngữ nghĩa ba nhánh

| Thái độ | Tính chất | Hình thức (phác) | Nguồn |
|---|---|---|---|
| **Belief proper** | Hướng về chân lý, là một disposition, không tự ý chọn được | `B(a, p)` | Cohen 1992; Engel 2000 |
| **Acceptance** | Một policy tự nguyện, gắn với ngữ cảnh hoặc mục đích; coi p là đúng cho một mục đích nào đó | `A(a, p, C)` | Cohen 1992; Maher 1993; Stalnaker 2014 |
| **Belief-in / faith** | Thái độ tin cậy, có đối tượng là một thực thể chứ không phải mệnh đề | `BelIn(a, x)` | Audi 2008, 2011 |

### Các quan hệ cấu trúc cần biểu diễn

- `Belief ⊆ Acceptance`: belief là một dạng của acceptance (Stalnaker).
- `A(a, p, C) ∧ ¬B(a, p)` là nhất quán: có acceptance mà không có belief (Clarke; Cohen).
- `A(a, p, C) ⊭ p`: acceptance không kéo theo p (Cohen, "Why Acceptance that P Does Not Entail that P").
- Belief là **default setting** của acceptance trong hội thoại (Stalnaker). Yalcin 2024 phản bác và đề xuất default là knowledge.

## A3. (Bản cũ) Thiết kế theo trục belief / acceptance

- **Confound cú pháp.** *believe that p* và *believe in X* khác khung cú pháp. Nếu stimuli khác khung, probe có thể chỉ học cú pháp chứ không học ontology.
- **Giải pháp cho trục belief / acceptance.** Cả hai cùng dùng khung *believe that p*, nên có thể làm minimal pair giữ nguyên cấu trúc, chỉ đổi ngữ cảnh:
  - giả thuyết làm việc trong nghiên cứu khoa học
  - phán quyết của bồi thẩm đoàn
  - luật sư chấp nhận một tiền đề để lập luận
  - giả định để chứng minh p sai (reductio)
- **Trục belief-in** khác khung cú pháp. Cần tách thành thí nghiệm riêng hoặc ghi rõ là giới hạn.
- **Giả thuyết kiểm chứng được** (từ Stalnaker): khi không có tín hiệu ngữ cảnh, biểu diễn của mô hình nghiêng về belief proper.
- **Ba câu hỏi, ba loại phương pháp:**
  - *represented* → linear probing
  - *separable* → activation patching / steering (kiểm tra tách biệt về mặt nhân quả)
  - *compositionally recoverable* → khôi phục các quan hệ hình thức ở mục 2 từ biểu diễn nội tại
- **Cầu nối sang tâm lý học:** Vesga, Van Leeuwen & Lombrozo (2025) có bằng chứng rằng người thường phân biệt belief epistemic và non-epistemic. Có thể hỏi LLM có tái tạo phân biệt này không.

## A4. (Bản cũ) Abstract theo belief / acceptance

> Large language models are increasingly analyzed as systems that encode attitudes such as beliefs, intentions, and values, yet the English word *belief* does not name a single attitude. Work in philosophy and pragmatics distinguishes belief proper — an involuntary, truth-directed disposition — from acceptance, a voluntary, context-relative policy of treating a proposition as true (Cohen 1992; Maher 1993; Engel 2000), and both from belief-in, a trusting attitude toward an object (Audi 2008). These attitudes share a lexical realization: *believe that p* can report either belief or acceptance, and acceptance without belief is coherent. We develop a formal semantic language that represents these relations as distinct — including the inclusion of belief within acceptance (Stalnaker 2014) and the failure of acceptance to entail belief — while preserving their common surface form. We then construct minimal pairs that hold the construction fixed and vary only the contextual cues that select the attitude, and map the formal representations onto the internal activations of [models]. Using [probing / activation patching / steering], we test whether the distinctions are represented, whether they are causally separable, and whether the formal relations between them can be recovered compositionally, including whether belief functions as the default reading of acceptance in the absence of contextual cues. [Key finding.] Restricting the study to a single lexical item gives a controlled setting that links linguistic and social ontology, formal semantics, and mechanistic interpretability, and yields a general method for testing whether formally specified semantic distinctions emerge in language models.

Placeholder cần điền: `[models]`, `[probing / activation patching / steering]`, `[Key finding.]`.

## 5. Tài liệu tham khảo

### I. Belief ↔ acceptance
1. **Perry, J. (1980).** "Belief and Acceptance." Belief đi qua acceptance đối với một câu hay that-clause; không coi *believe that p* là primitive. → Hợp với phần related work hơn là abstract.
2. **Maher, P. (1993).** "The Concept of Acceptance." Trong *Betting on Theories*. Acceptance là trạng thái được biểu hiện qua một assertion chân thành. Trích: *"What I am here calling acceptance is commonly called belief."* → Khái niệm "belief" thông thường có chứa acceptance.
3. **Cohen, L. J. (1992).** *An Essay on Belief and Acceptance.* Belief là disposition không tự ý chọn được; acceptance là policy tự nguyện. Ví dụ: tri thức khoa học, phán quyết bồi thẩm.
4. **Engel, P. (2000).** "Introduction: The Varieties of Belief and Acceptance." Trong *Believing and Accepting.* Phân biệt believing proper, holding true, accepting. Acceptance mang tính thực tiễn, gắn với ngữ cảnh, và có thể dựa trên belief.
5. **Clarke, D. S.** "The Possibility of Acceptance Without Belief." Trong *Believing and Accepting.* Trường hợp `A(p) ∧ ¬B(p)`.

### II. Stalnaker và common ground
6. **Stalnaker, R. (2014).** *Context*, đặc biệt "Common Ground and Keeping Score." Acceptance là khái niệm rộng hơn belief; belief là default setting.
7. **Yalcin, S. (2024).** "Defining Common Ground." Đề xuất common ground là common knowledge về những gì được accept, và default là knowledge chứ không phải belief. → Chỉ cần nếu bài có đụng tới common ground.
8. **Michaelson, E. & Stokke, A. (2018).** "Common Ground." Trong *Lying and Insincerity.* Common ground định nghĩa qua acceptance chứ không qua belief, nhờ đó giải thích được bald-faced lies.

### III. Belief không đồng nhất
9. **Audi, R. (2008).** "Belief, Faith, and Acceptance." Phân biệt propositional belief, objectual belief, belief-in (trusting). Trích: *"sometimes the term 'belief' is used where 'faith' or 'acceptance' would better express what is intended."*
10. **Audi, R. (2011).** "Belief, Faith, Acceptance, and Hope." Trong *Rationality and Religious Commitment.* Faith là thái độ nhận thức không đồng nhất với belief.

### IV. Tâm lý học thực nghiệm
11. **Vesga, Van Leeuwen & Lombrozo (2025).** "Evidence for Multiple Kinds of Belief in Theory of Mind." Bằng chứng thực nghiệm cho phân biệt belief epistemic và non-epistemic.

## 6. Ước tính chi phí

### 6.0 Bản tính lại theo đề bài đã chốt (2026-09-27) — dùng bản này

Giá GPU và giá Prolific theo hiểu biết của Claude, chưa kiểm tra giá hiện tại, có thể lệch ±30%.

**Những gì thay đổi so với bản cũ (6.1 trở xuống):**
- Mô hình tối thiểu phải **≥ 7B**, vì hành vi belief chỉ xuất hiện từ khoảng 7B (Steele et al. 2026b).
- Ngữ cảnh dài hơn (đoạn hội thoại khoảng 150–300 token, thay vì câu dưới 64 token), nên **người đánh giá mất nhiều thời gian hơn**: khoảng 45 giây mỗi item thay vì 20 giây.
- Nhãn dạng liên tục cần **nhiều người đánh giá hơn** mỗi item (5 thay vì 3) để ước lượng được mức đồng thuận.
- Có thêm **mẫu tự nhiên** cần gán nhãn.
- Dùng lại code DAS / patching của Steele et al., nên công viết code giảm.
- **Kết quả: người đánh giá trở thành khoản chi lớn nhất, không còn là GPU.**

Giả định tính toán: Prolific ≈ $12/giờ + ~33% phí ≈ **$16/giờ-người**; GPU H100 ≈ $2–2.5/giờ.

| Hạng mục | Giai đoạn 0: Pilot | Giai đoạn 1: Tối thiểu (workshop) | Giai đoạn 2: Đầy đủ (hội nghị) |
|---|---|---|---|
| Stimuli | 30 cặp, 3–4 miền | 300–500 cặp, 5 miền | 1.500 cặp, 8 miền + 800 mẫu tự nhiên |
| Mô hình | 1 × 7B | 2 × 7–8B | 4 mô hình, có 1 × 70B |
| Mức đo | Hành vi | Hành vi + probe + patching / DAS | Cả ba mức + hình học "kinds vs continua" |
| **Người đánh giá** | 60 item × 10 người × 45s ≈ 7,5h → **~$120** (hoặc tự nhờ bạn bè: $0) | 1.000 item × 3–5 người × 45s ≈ 37–62h → **$600–1.000** | 3.000 item × 5 × 45s ≈ 190h → ~$3.000; mẫu tự nhiên 800 × 3 × 40s ≈ 27h → ~$430. **Tổng ~$3.400** |
| **GPU** | vài giờ → **$0–20** (Colab Pro / cluster trường) | 30–60h → **$75–150** | 250–400h → **$600–1.000** (70B chạy qua NDIF thì giảm mạnh) |
| Sinh nháp stimuli bằng LLM API | ~$5 | ~$30 | ~$80 |
| Đo hành vi mô hình đóng qua API (tùy chọn) | — | ~$30 | ~$100 |
| Thí nghiệm người làm baseline kiểu Vesga et al. (tùy chọn) | — | — | 150 người × 15 phút ≈ **$600** |
| Dự phòng (+20%) | ~$30 | ~$150–250 | ~$1.000 |
| **Tổng** | **~$0–180** | **~$900–1.500** | **~$5.000–6.000** (không có baseline: ~$4.500) |

**Cách giảm tiền người đánh giá, khoản lớn nhất:**
- 3 người mỗi item thay vì 5. Chỉ dùng 5 người cho khoảng 20% item để ước lượng mức đồng thuận.
- Lọc stimuli trước bằng một vòng nhỏ, chỉ đưa những item qua được đi đánh giá đầy đủ.
- Người đánh giá là sinh viên hoặc tình nguyện viên trong trường.
- **Không dùng LLM làm người đánh giá cho nhãn chính.** Dùng LLM gán nhãn để kiểm tra chính LLM là vòng tròn. Chỉ dùng LLM để sinh nháp stimuli.

**Lưu ý thủ tục:** thu thập đánh giá từ người, đặc biệt qua Prolific, có thể cần IRB của trường duyệt (thường là diện exempt). Nên tính thêm vài tuần.

**Thời gian (bán thời gian, một người):**

| Việc | Thời gian |
|---|---|
| Formalize (khung quyết định, hai cơ chế con) | 2–3 tuần |
| Thiết kế + kiểm định stimuli (phần khó nhất) | 1,5–2 tháng |
| Thí nghiệm (dùng lại code Steele et al.) | 1,5–2 tháng |
| Viết bài | 1 tháng |
| **Tổng** | **~4–6 tháng** (+ thời gian IRB nếu cần) |

---

### 6.1 Bản cũ (theo trục belief / acceptance, trước khi chốt đề bài)

Giá GPU và giá Prolific theo hiểu biết của Claude, chưa kiểm tra giá thị trường hiện tại, có thể lệch ±30%. Chi phí lớn nhất là thời gian người làm; tiền mặt khá thấp.

### Giả định
- Dùng mô hình open-weights để can thiệp được vào activation. API đóng không làm được mechanistic interpretability.
- A100 80GB khoảng $1.5–2/giờ, H100 khoảng $2–3/giờ (RunPod, Lambda…).
- Prolific: khoảng $12/giờ, cộng phí nền tảng khoảng 33%.
- Stimuli ngắn (dưới 64 token), nên mỗi lần chạy mô hình rất rẻ.

### Ba mức

| Hạng mục | Tối thiểu (pilot / workshop) | Vừa (bài hội nghị) | Đầy đủ |
|---|---|---|---|
| Mô hình | 1–2 mô hình 7–9B | 3–4 mô hình, có 1 mô hình ~70B | Nhiều họ mô hình, nhiều kích cỡ |
| Số minimal pair | ~500 | 1.500–2.000 | 3.000+ |
| Phương pháp | Probing + patching cơ bản | + steering, test compositional | + train SAE, ablation, kiểm tra độ bền |
| GPU (giờ) | 20–40 | 150–250 | 800–1.500 |
| **Chi GPU** | **$50–100** | **$400–800** | **$2.500–5.000** |
| Sinh stimuli bằng LLM API | ~$20 | ~$50 | ~$100–200 |
| Kiểm định stimuli (3 người gán nhãn mỗi câu) | ~$150 | $400–600 | $800–1.200 |
| Thí nghiệm trên người làm baseline | Không làm | ~$400 (khoảng 100 người × 15 phút) | $1.000–2.000 |
| Dự phòng chạy lại, debug (+30%) | ~$70 | ~$400 | ~$1.500 |
| **Tổng** | **~$300–400** | **~$1.700–2.300** | **~$6.000–10.000** |

### Vì sao GPU tốn ít
- **Probing:** trích activation một lần rồi train classifier trên CPU; vài phút GPU cho mỗi mô hình.
- **Activation patching:** phần tốn nhất. Ví dụ 32 layer × ~20 vị trí token × 1.000 cặp câu ≈ 640 nghìn lượt forward, tức vài giờ H100 cho mỗi mô hình 8B. Mô hình 70B tốn khoảng 10 lần, cần 2 H100 hoặc chạy lượng tử hóa.
- **Train SAE** là thứ đẩy chi phí lên mức "đầy đủ". Dùng SAE có sẵn (Gemma Scope, Llama Scope) thì gần như không tốn thêm.

### Cách giảm gần về 0
- **NDIF** (National Deep Inference Fabric), dùng qua `nnsight`: truy cập miễn phí từ xa các mô hình lớn để can thiệp vào activation.
- Cluster của trường, hoặc tín dụng nghiên cứu (Google TRC, academic credits của các nhà cung cấp cloud).
- Colab Pro (~$10/tháng) đủ cho mức tối thiểu.
- Dùng SAE có sẵn thay vì tự train.

### Thời gian (bán thời gian, một người)
- Ngôn ngữ hình thức: 1–2 tháng.
- Thiết kế và kiểm định stimuli: 1–1,5 tháng. Đây là phần dễ bị đánh giá thấp nhất.
- Thí nghiệm mechanistic: 1,5–3 tháng.
- Viết bài: 1 tháng.
- **Tổng: khoảng 5–8 tháng.**

### Khuyến nghị
Bắt đầu ở mức tối thiểu: 1 mô hình 8B, 300–500 cặp câu, chỉ probing trục belief / acceptance. Dưới $100, biết ngay tín hiệu có tồn tại hay không trước khi mở rộng.

## 7. Kiểm chứng novelty (2026-09-27)

Phạm vi: khoảng 10 lượt tìm web (arXiv, PhilPapers…), chỉ đọc abstract. Chưa quét hết ACL Anthology hay OpenReview. Kết luận là "chưa tìm thấy", không phải "chắc chắn chưa ai làm".

### Kết luận
**Chưa thấy công trình nào** kiểm tra, bằng phương pháp mechanistic, xem LLM có phân biệt belief proper và acceptance (theo nghĩa Cohen / Maher) khi **giữ nguyên khung *believe that p***, cùng chủ thể, cùng mệnh đề, chỉ đổi ngữ cảnh. Cũng chưa thấy bài nào nối ngôn ngữ hình thức cho các loại thái độ này với biểu diễn nội tại.

### Công trình gần nhất và khác biệt

| Công trình | Làm gì | Khác dự án ở đâu | Mức đe dọa |
|---|---|---|---|
| **Steele, Wen & Han (2026a)**, "One mechanism for many mental spaces", arXiv 2607.10248 | Một "router" hạng thấp trên một value slot dùng chung, phân biệt các không gian belief / counterfactual / fictional / temporal. DAS trên một loại không gian điều khiển được cả các loại khác. | Phân biệt *không gian nội dung* (giá trị trong niềm tin so với thực tế), không phải *loại thái độ* của cùng chủ thể với cùng p. | **Cao nhất.** Reviewer sẽ hỏi: acceptance có phải chỉ là một "space" kiểu supposition không? |
| **Steele, Wen & Han (2026b)**, "Belief-reality separation lives in routing…", arXiv 2607.11945 | Cơ chế tách niềm tin của nhân vật khỏi thực tế. | Chỉ một loại belief (ToM). | Trung bình |
| **Nguyen & Salim (2026)**, "Whether LLMs Can Navigate Beliefs and Facts Depends on How You Phrase It", arXiv 2608.17809 | 18 cách diễn đạt epistemic, 10 LLM; hành vi + attention + can thiệp. | Thay đổi *cách diễn đạt*, không giữ nguyên khung; không có phân loại belief / acceptance. | Trung bình |
| **Suzgun et al. (2024/2025)**, "Belief in the Machine" (KaBLE), arXiv 2410.21195 | Hành vi: fact / belief / knowledge. | Chỉ hành vi; phân biệt belief với knowledge, không với acceptance. | Thấp |
| **Zhu et al. (2024)**, "Language Models Represent Beliefs of Self and Others", arXiv 2402.18496 | Probing belief trong ToM. | Belief *của ai*, không phải *loại* belief. | Thấp |
| **Sturgeon, Africa & Black (2026)**, "When Role-playing, Do Models Believe What They Say?", arXiv 2606.11502 | Truth probe: nhập vai có thay đổi biểu diễn chân lý của chính mô hình không. | Thái độ của *mô hình*, không phải ngữ nghĩa của câu tường thuật thái độ. | Thấp |
| Herrmann & Levinstein; Chalmers (2025) "Propositional Interpretability" | Tiêu chuẩn để LLM *có* belief. | Câu hỏi khác: mô hình có belief không, chứ không phải mô hình biểu diễn *nghĩa* của "belief" ra sao. | Thấp, nhưng nên trích |
| **Vesga, Van Leeuwen & Lombrozo (2025)**, JEP: General | Người thường phân biệt belief epistemic / non-epistemic (3 nghiên cứu, 1.843 người). | Trên người, không trên LLM. | Không đe dọa, là **cơ hội**: chưa ai hỏi LLM có tái tạo phân biệt này không. |

### Quét ACL Anthology và OpenReview (2026-09-27)

**ACL Anthology:** tải toàn bộ file `anthology+abstracts.bib` (131.152 bài, 82.464 bài có abstract) rồi lọc bằng regex trên tiêu đề và abstract:
- belief + acceptance + (attitude / doxastic / epistemic / common ground / supposition) + LLM → **0 bài** đúng chủ đề.
- cụm "belief vs/and acceptance" → **0 bài**.
- "kinds / types / varieties of belief", "belief-in", "non-epistemic belief" → 3 bài, không liên quan.
- belief + (probe / activation / patching / steering / interpretability) + LLM → 33 bài, đọc tay tiêu đề. Các bài liên quan ở bảng dưới.

Giới hạn: khoảng 37% bài trong Anthology không có abstract trong file, nên chỉ lọc được theo tiêu đề.

**OpenReview:** API tìm kiếm (`api2.openreview.net/notes/search`) trả về chủ yếu kết quả từ DBLP, không dùng được. Chỉ tìm bằng web search giới hạn domain. Đây là **phần yếu nhất** của việc quét: có thể sót submission ICLR / NeurIPS chưa lên arXiv.

| Công trình mới tìm thêm | Làm gì | Liên quan thế nào |
|---|---|---|
| **Ying, Zhi-Xuan, Wong, Mansinghka & Tenenbaum**, "Understanding Epistemic Language with a Language-augmented Bayesian Theory of Mind", TACL (trình bày tại NAACL 2025) | Dịch câu epistemic sang một language-of-thought hình thức, đánh giá bằng Bayesian ToM; belief là xác suất. | **Chính là "foil"** mà abstract nhắc tới ("single probabilistic interpretation"). Có ngôn ngữ hình thức nhưng không phân biệt belief / acceptance, không xét biểu diễn nội tại của LLM. Nên trích và đặt đối lập. |
| **Kouwenhoven, van der Meer & van Duijn (2026)**, "Traces of Social Competence in LLMs", CoNLL 2026 | 17 mô hình, 192 biến thể false-belief; steering tách được một **vector "think"** là nguyên nhân gây hành vi. | Tiền lệ phương pháp (steering theo động từ thái độ). Đồng thời cho thấy **từ vựng trạng thái tâm lý tự nó điều khiển hành vi**, nên càng phải giữ nguyên từ *believe* trong minimal pair. |
| **"It's Not What You Say, It's How You Say It: Evaluating LLM Responses to Expressions of Belief"**, ACL 2026 | Phân loại 17 kiểu biểu đạt niềm tin (form, evidentiality, epistemic stance, tone); 16 mô hình; chỉ đo hành vi. | Thay đổi *hình thức biểu đạt*; không phân biệt loại thái độ; không xét nội tại. |
| **Corona Mendozza & Søgaard (2026)**, "LLM Beliefs Are in Their Heads", ACL 2026 | Probe + steering theo tiêu chí Herrmann & Levinstein. | Belief *của mô hình*, không phải nghĩa của câu tường thuật belief. |
| **Bortoletto et al. (2025)**, "Brittle Minds, Fixable Activations", Findings EMNLP 2025 | Probe biểu diễn belief trong ToM; sửa activation để sửa suy luận ToM. | Belief *của ai*, không phải *loại* belief. |
| **Cheng, Hawkins & Jurafsky (2026)**, "Accommodation and Epistemic Vigilance", arXiv 2601.04435 | Dùng lý thuyết ngữ dụng (accommodation) giải thích vì sao LLM không phản bác niềm tin sai của người dùng; chỉ đo hành vi. | Liên quan nhánh Stalnaker / common ground, nhưng không phân biệt belief / acceptance. |
| **Prakash et al.**, "Language Models Use Lookbacks to Track Beliefs" (OpenReview) | Cơ chế theo dõi belief trong ToM. | Cùng nhóm với Steele et al.: *ai* tin *gì*. |

**Kết luận sau khi quét: không thay đổi.** Vẫn chưa thấy công trình nào phân biệt belief proper và acceptance trong biểu diễn nội tại của LLM. Lĩnh vực "belief trong LLM" rất đông, nhưng gần như toàn bộ xoay quanh ba câu hỏi khác: (1) belief *của ai* (ToM), (2) mô hình *có* belief không, (3) *cách diễn đạt* ảnh hưởng hành vi thế nào.

### Đọc toàn văn Steele, Wen & Han (2026a, b) — 2026-09-27

Cả hai là preprint arXiv (7/2026), chưa qua bình duyệt, cùng một nhóm tác giả. Đã đọc toàn bộ phần chính của cả hai bài; chưa đọc appendix của bài b.

**Bài a — "One mechanism for many mental spaces" (2607.10248)**
- Stimuli: 1 thực thể, 2 giá trị màu, một ở thực tế, một ở "không gian" khác. Có 9 loại builder: painting, belief (`{Name} believes the {entity} is {c}`), dream, movie, past, yesterday, hypothetical, modal, reported speech.
- Mô hình: Qwen2.5-3B (chính), Pythia-2.8b, Falcon3-3B; phần composition dùng 7B/14B.
- Phương pháp: probe tuyến tính, logit lens, DLA, **DAS** (rank ≤ 4 đủ điều khiển hoàn toàn). Steering bằng diff-of-means **không vượt được** hướng ngẫu nhiên cùng norm, nên mọi kết luận nhân quả đều dựa trên DAS.
- Kết quả chính: một "router" (space index) hạng thấp **dùng chung** cho mọi loại không gian. DAS học trên một loại điều khiển được các loại khác (transfer index 0.71–0.89).
- §4.11: phân loại thô vẫn còn (attitude report / intensional / temporal / fictional; trong lớp 0.89–0.92 so với giữa lớp 0.53–0.76), nhưng **belief không tách riêng khỏi counterfactual**.
- §4.10: ghép builder (vd. "used to believe") thì **tạo router mới** trên value slot dùng chung.
- Tự nhận giới hạn:
  - Không kiểm tra referential opacity.
  - "Whether two marked spaces' routers dissociate pairwise is open."
  - "Whether the built router has an independently recoverable constituent structure (belief + tense) is left open."

**Bài b — "Belief–reality separation…" (2607.11945)**
- Belief ↔ reality: value slot **không mang nhãn frame** (transfer chéo 0.87–0.95); việc phân biệt nằm ở **router tại vị trí query**. Router belief và router reality tách nhau (chéo ≤ 0.16–0.20) và gần trực giao.
- Belief asserted và belief derived (qua visibility, lookback của Prakash et al.) dùng chung một slot.
- **Hành vi này chỉ xuất hiện từ khoảng 7B trở lên** (ở 3B thất bại do recency).
- Router học trên *believes* chuyển được sang *reckons* và *is convinced*: router gắn với loại frame, không gắn với động từ cụ thể.
- Câu query trống mặc định đọc ra **reality**.
- Mô hình: Qwen2.5 7B/14B, Mistral-7B, OLMo-2-7B.
- **Công bố sẵn corpus và code:** HF `osteele/mental-spaces`, GitHub `osteele/mental-spaces`.

**Đánh giá lại mức đe dọa: từ "đe dọa" thành "nền móng".**
- Họ coi *belief là một loại duy nhất*. Không có acceptance, supposition-for-a-purpose, belief-in, và không có trục loại thái độ bên trong họ doxastic.
- Họ để ngỏ đúng hai câu hỏi mà dự án này hỏi: (1) router của hai không gian "marked" có tách nhau không; (2) router ghép có cấu trúc thành phần khôi phục được không. Câu (2) trùng với mục tiêu "compositionally recoverable".
- **Rủi ro thật:** kết quả của họ gợi ý mô hình chỉ giữ phân biệt ngữ nghĩa ở mức thô. Phân biệt belief / acceptance, vốn mịn hơn belief / counterfactual, có thể ra **null**. Cần thiết kế để null vẫn diễn giải được, dùng belief vs reality và belief vs hypothetical làm đối chứng dương.

**Thiết kế cụ thể rút ra: mở rộng paradigm slot / router của họ**
- Câu có **ba giá trị cùng tồn tại** để kiểm tra `A ∧ ¬B` và `A ⊭ p`, ví dụ: "For the trial, the juror accepts the cup is blue. Privately, she believes it is green. In reality it is red." Query theo từng frame.
- Kiểm tra:
  - Router acceptance có tách khỏi router belief không, hay trùng với router hypothetical?
  - `Belief ⊆ Acceptance` dự đoán **transfer bất đối xứng**: router belief chuyển sang acceptance mạnh hơn chiều ngược lại. Đây là dự đoán cụ thể, có thể sai.
  - Câu query trống kiểu "The juror thinks…" mặc định đọc ra belief hay acceptance? Đây là phiên bản kiểm chứng được của default setting theo Stalnaker.
- **Hai tầng stimuli:**
  - (i) Khác động từ: *believes* vs *accepts / assumes / supposes*. Dễ làm, mở rộng trực tiếp bài của họ.
  - (ii) Cùng động từ *believes*, ngữ cảnh chọn cách đọc acceptance. Đây mới là điểm mới cốt lõi, nhưng khó: phải kiểm định bằng người rằng *believe* thật sự có cách đọc acceptance trong ngữ cảnh đó.
- **Belief-in (Audi) không vừa paradigm này**, vì không có giá trị thuộc tính để đọc ra. Để riêng.

**Hệ quả cho chi phí (§6):**
- Mức tối thiểu phải dùng **mô hình ≥ 7B**; 3B không làm được hành vi belief.
- DAS rẻ (~150 bước, rank 8), và dùng lại được corpus + code của họ, nên chi phí sinh stimuli và công viết code giảm đáng kể.

### Quét lại theo đề bài đã chốt: truth-seeking vs vì giá trị (2026-09-27)

Phạm vi:
- Khoảng 6 lượt web search (non-epistemic belief, practical reasons for belief, motivated / wishful belief, hope vs believe, credence).
- Lọc lại toàn bộ file bib của ACL Anthology bằng regex với các từ khóa này.
- Chỉ đọc abstract. OpenReview vẫn chặn truy cập tự động.

**Kết luận: chưa thấy công trình nào hỏi LLM có phân biệt niềm tin truth-seeking với niềm tin vì giá trị khi *gán cho một chủ thể*, dù ở mức hành vi hay mức biểu diễn.**

ACL Anthology: với các cụm non-epistemic / pragmatic belief, practical reasons for belief, will to believe, hope ↔ believe, credence, senses of believe → **0 bài liên quan**.

Các cụm công trình gần nhất:

| Cụm | Ví dụ | Khác đề bài ở đâu |
|---|---|---|
| **Mô hình *tự nó* có motivated reasoning / wishful thinking không** | Yongsatianchot & Marsella, "Investigating Motivated Inference in LLMs", WiNLP 2025 (hành vi; mô hình ít wishful thinking trừ khi được nhắc "hopeful"); "Detecting Motivated Reasoning in Internal Representations" (OpenReview; bias do gợi ý trong CoT, đọc được bằng probe); "Persona-Assigned LLMs Exhibit Human-Like Motivated Reasoning", Findings ACL 2026 | Mô hình là *người tin*. Đề bài hỏi mô hình *hiểu* niềm tin vì giá trị của người khác. Cũng khác về bản chất: motivated reasoning làm *méo credence*, còn niềm tin vì giá trị *giữ nguyên credence thấp*. |
| **Biểu đạt epistemic như một thang độ chắc chắn** | Li, Vrazitulis & Schlangen, "Representations of Fact, Fiction and Forecast in LLMs", ACL 2025; Suzgun et al. (KaBLE); Nguyen & Salim 2026; "It's Not What You Say…" ACL 2026 | Coi *believe* là **một điểm trên thang chắc chắn**, tức đúng cách hiểu "belief = xác suất" mà đề bài muốn kiểm tra. Nên trích làm đối chứng. |
| **Phía người** | Vesga, Van Leeuwen & Lombrozo 2025 (JEP: General); Van Leeuwen 2014 "Religious credence is not factual belief"; Mugg 2025 "Factual Belief and Religious Credence: Kinds or Continua?" (*Philosophia*) | Trên người, không trên LLM. Lưu ý: "non-epistemic" của Vesga et al. nhấn vào vai trò xã hội / tín hiệu nhóm, **không trùng hẳn** với "tin vì kết cục tốt hơn" của đề bài. Cần nói rõ chỗ trùng và chỗ khác. |
| **Cơ chế** | Steele, Wen & Han 2026a, b | Belief là một loại duy nhất (xem trên). |

**Hai hàm ý mới:**
1. **Đối chứng rõ ràng:** mảng "epistemic expressions" đang coi *believe* là một mức độ chắc chắn. Giả thuyết "mô hình gộp credence và niềm tin vì giá trị làm một" chính là phiên bản kiểm chứng được của cách hiểu đó.
2. **Câu hỏi "kinds hay continua"** (Mugg 2025 phản biện Van Leeuwen) có thể đưa vào đo trực tiếp. Hình học biểu diễn trong mô hình là hai cụm rời hay một trục liên tục? Đây là đóng góp ngược lại cho triết học.

### Hàm ý cho định vị bài
- **Biến mối đe dọa thành giả thuyết:** acceptance dùng lại router / space index của Steele et al. (tức acceptance ≈ một không gian giả định), hay có một chiều riêng? Cả hai kết quả đều công bố được.
- **Điểm mới cần nhấn mạnh:** (1) giữ nguyên cấu trúc bề mặt, chỉ đổi loại thái độ; (2) ngôn ngữ hình thức có tiên đề (Belief ⊆ Acceptance, A ∧ ¬B, A ⊭ p) làm tiêu chuẩn cho test compositional; (3) nối với bằng chứng tâm lý học của Vesga et al.
- Tránh tự nhận "first to study belief in LLMs": vùng đó đã rất đông.

### Trích dẫn đã kiểm chứng
- Yalcin (2024), "Defining common ground", *Linguistics and Philosophy* 47: 1045–70. ✔
- Vesga, Van Leeuwen & Lombrozo (2025), *Journal of Experimental Psychology: General*, online tháng 5/2025. ✔

## 8. Việc cần làm

- [x] **Quét lại novelty theo đề bài đã chốt** (xem §7, mục "Quét lại theo đề bài đã chốt").
- [ ] Đọc toàn văn Li, Vrazitulis & Schlangen (ACL 2025) và Mugg (2025).
- [ ] Đọc Vesga, Van Leeuwen & Lombrozo (2025) toàn văn. Đây là nguồn gần nhất với đề bài (phía người), có thể mượn stimuli và thước đo.

- [x] Kiểm tra năm, venue của Yalcin 2024 và Vesga et al. 2025.
- [x] Đọc toàn văn Steele et al. 2026a, b (trừ appendix bài b).
- [ ] Clone `osteele/mental-spaces`, chạy lại thí nghiệm belief vs reality trên một mô hình 7B làm pilot.
- [ ] Viết 20–30 câu mẫu tầng (ii) (*believe* đọc theo nghĩa acceptance), kiểm định nhanh bằng người trước khi làm quy mô lớn.
- [x] Quét ACL Anthology (toàn bộ file bib) và OpenReview (chỉ qua web search).
- [ ] OpenReview còn yếu: tìm tay trên openreview.net cho ICLR / NeurIPS 2025–2026 (từ khóa: acceptance, supposition, attitude verb, doxastic).
- [ ] Đặt Ying et al. (LaBToM) làm đối chứng "belief = xác suất" trong phần related work.
- [ ] Phác cú pháp và ngữ nghĩa cho ngôn ngữ hình thức: `B`, `A_C`, `BelIn` và các tiên đề nối chúng.
- [ ] Thiết kế bộ minimal pair cho trục belief / acceptance.
- [ ] Quyết định cách xử lý trục belief-in (thí nghiệm riêng hay ghi là giới hạn).
- [ ] Chọn mô hình và phương pháp; điền placeholder trong abstract.

## 9. Pilot mức 1 — hành vi (chạy 2026-09-27)

**Code:** `pilot/stimuli.py` (sinh `stimuli.jsonl`), `pilot/run.py`, `pilot/analyze.py`. Kết quả thô: `pilot/results_*.jsonl`.
**Chạy lại:** `.venv/bin/python pilot/run.py <mlx model> <out.jsonl>` rồi `.venv/bin/python pilot/analyze.py <out.jsonl>`.

**Thiết kế:**
- 24 item, 4 miền. Mỗi item 3 điều kiện, dùng chung câu đích "X believes that p.":
  - TS = bằng chứng tốt;
  - IR = bằng chứng xấu, không có lợi ích từ việc tin;
  - VD = IR + **một câu** nói việc tin giúp kết cục tốt hơn.
- 3 câu hỏi Yes/No; đo P(Yes) chuẩn hóa trên token đầu.
- Thêm điều kiện đối chứng hỏi credence khi **không có** câu belief, để đo mức dịch chuyển do chính câu belief gây ra.
- Mô hình: Qwen2.5-7B-Instruct và Qwen3-4B-Instruct-2507, cả hai 4-bit MLX, chạy trên M1 Pro.

**Kết quả: P(Yes), trung bình qua 24 item**

| Câu hỏi | Kỳ vọng TS / VD / IR | Qwen2.5-7B TS / VD / IR | Qwen3-4B TS / VD / IR |
|---|---|---|---|
| Nghĩ là *likely*? (credence) | Y / **N** / Y | 1.00 / **0.71** / 0.27 | 1.00 / **1.00** / 0.80 |
| Niềm tin có *reasonable*? | Y / **Y** / N | 0.94 / **0.44** / 0.08 | 1.00 / **0.63** / 0.18 |
| Bỏ niềm tin nếu có bằng chứng xấu? | Y / **N** / N | 0.76 / **0.11** / 0.52 | 0.52 / **0.06** / 0.56 |

Kiểm định cặp VD − IR (Wilcoxon, n = 24): mọi khác biệt chính đều p < 0.001 trên cả hai mô hình.

**Đọc kết quả:**
1. **Mô hình nhận ra phần chức năng của niềm tin vì giá trị.**
   - Niềm tin VD bền với bằng chứng xấu: P(bỏ niềm tin) VD 0.11 so với TS 0.76 (7B).
   - Niềm tin VD được đánh giá hợp lý hơn IR rõ rệt (+0.36 ở 7B, +0.46 ở 4B).
2. **Nhưng mô hình gộp nó với credence.**
   - Ở VD, mô hình cho rằng người đó *nghĩ là likely* (7B: 0.71, 4B: 1.00), **cao hơn cả IR** (+0.44 và +0.20).
   - Câu "believes that p" đẩy credence lên mạnh nhất chính ở VD: +0.60 (7B), +0.71 (4B) so với khi không có câu đó.
   - Tức là "believes" vẫn bị đọc thành "thấy có khả năng cao", đúng dạng collapse mà giả thuyết đặt ra. Bản 4B collapse hoàn toàn.
3. **Mức "reasonable" của VD** chỉ ở khoảng giữa (0.44 / 0.63), chưa đến mức TS.

**Giới hạn — kết quả này CHƯA dùng để kết luận được:**
- **Chưa có đường chuẩn của người.** Việc VD phải được trả lời "No" ở câu credence là theo khung của đề bài. Người đọc thật có thể trả lời khác. Đây là việc cần làm tiếp quan trọng nhất.
- **Nhiễu từ vựng:** câu stake dùng chữ "convinced", có thể tự nó đẩy câu trả lời credence lên. Cần biến thể stake không có từ vựng niềm tin, và một đối chứng thêm câu trung tính cùng độ dài.
- Stimuli do Claude viết, chưa được người kiểm định. Chỉ có 1 template câu hỏi, dạng Yes/No, mô hình instruct lượng tử hóa 4-bit, n = 24. Nhóm cơ chế (b) chỉ có 8 item.
- Kết quả IR ở 7B lệch khỏi kỳ vọng (credence 0.27, kỳ vọng "Yes"): mô hình có vẻ neo theo bằng chứng hơn là theo câu belief.

**Bước tiếp theo:**
- [ ] Đường chuẩn người trên đúng 72 cặp ngữ cảnh × câu hỏi này (tự làm hoặc nhờ 5–10 người).
- [ ] Biến thể stake không dùng "convinced" / "believe" + đối chứng câu trung tính cùng độ dài.
- [ ] Thêm 2–3 cách diễn đạt câu hỏi; thêm mô hình base (dạng completion).

### 9.1 Đối chứng từ vựng (chạy 2026-09-27)

Thêm 2 điều kiện:
- **VDn:** câu stake bỏ "convinced / conviction", thay bằng "committed to the idea that".
- **IRf:** IR + một câu trung tính dài tương đương.

| Credence P(Yes) | VD | VDn | IR | IRf |
|---|---|---|---|---|
| Qwen2.5-7B | 0.71 | **0.70** | 0.27 | 0.16 |
| Qwen3-4B | 1.00 | **0.96** | 0.80 | 0.73 |

- **VDn ≈ VD** (7B: −0.01, p = 0.88; 4B: −0.04, p = 0.60). Chữ "convinced" **không** phải thứ đẩy credence lên.
- **IRf ≤ IR:** thêm một câu bất kỳ không làm credence tăng.
- Hai câu hỏi "reasonable" và "evidence" cũng gần như không đổi giữa VD và VDn.

→ **Việc credence tăng ở VD đến từ *nội dung* câu stake** (việc tin có ích), không phải từ từ vựng hay độ dài. Kết quả gộp belief với credence vững hơn sau đối chứng này.

Giới hạn còn lại: "committed to the idea that" vẫn là một cụm chỉ thái độ. Câu stake mô tả "những người tin p thì có kết cục tốt", nên mô hình có thể suy ra "cô ấy thuộc nhóm đó, tức là thấy p có khả năng". Dù vậy, đây chính là câu hỏi của đề bài: tin vì giá trị có kéo theo credence cao không. Muốn biết câu trả lời "đúng" thì cần đường chuẩn của người.

### 9.2 Form thu đường chuẩn người (2026-09-27)

- **Link:** https://claude.ai/artifact/Px4QJULqA4zcM4oriUoywV (đang ở chế độ private; phải mở chia sẻ trong menu Share thì người khác mới xem được).
- **Nguồn:** `pilot/human_form.template.html` + `pilot/build_form.py` sinh ra `pilot/human_form.html` từ chính `stimuli.py`.
- **Thiết kế:**
  - 3 danh sách Latin square: mỗi người thấy mỗi item ở đúng một điều kiện TS / VD / IR. Muốn chọn danh sách cụ thể thì thêm `#l1`, `#l2`, `#l3` vào cuối link; không thêm thì chọn ngẫu nhiên.
  - 24 đoạn + 2 câu kiểm tra chú ý; 3 câu hỏi mỗi đoạn, thang 1–7. Khoảng 15 phút.
  - Không gửi dữ liệu tự động: người làm bấm **Copy results** rồi gửi đoạn JSON.
- **Thu dữ liệu:** lưu mỗi người thành `pilot/human/<tên>.json`, rồi chạy `.venv/bin/python pilot/human.py pilot/results_qwen25_7b.jsonl pilot/results_qwen3_4b.jsonl`. Script tự loại người trượt câu kiểm tra, quy điểm về thang 0–1, và so với P(Yes) của mô hình.
- **Mục tiêu tối thiểu:** 9 người (3 người mỗi danh sách), tức mỗi ô item × điều kiện có 3 đánh giá.
