# Git Commit Log - Lab 04

## Commit History

*(Sau khi hoàn thành các lệnh git commit theo từng phase, bạn có thể chạy lệnh sau trong terminal để tự động cập nhật file này:)*
```bash
git log --oneline --decorate --graph -n 10
```

---

### Example Commit Chain (Theo chuẩn Spec Kit):

#### Commit 1: Phase 1 (Spec & Data Models)
- **Message:** `feat(phase-1): define data models and October 2026 ground-truth dataset`
- **Scope:** Khởi tạo `.specify/spec.md`, `sample_data.py`, khai báo `Transaction` dataclass.

#### Commit 2: Phase 2 (Design Plan & Diagrams)
- **Message:** `docs(phase-2): add architecture plan and Mermaid design artifacts`
- **Scope:** Hoàn thiện `.specify/plan.md` với 4 sơ đồ Mermaid (Activity, Sequence, State Machine, Class Diagram).

#### Commit 3: Phase 3 (Task Breakdown)
- **Message:** `docs(phase-3): add decomposed task checklist for vibe-coding`
- **Scope:** Tạo `.specify/tasks.md`.

#### Commit 4: Phase 4 (Implementation & Testing)
- **Message:** `feat(phase-4): implement classification engine and pass October unit tests`
- **Scope:** Hoàn thiện `tracker.py`, sửa lỗi làm tròn boundary threshold, `test_tracker.py` pass 100%.

#### Commit 5: Phase 5 (Streamlit Dashboard)
- **Message:** `feat(phase-5): implement interactive Streamlit budget monitor dashboard`
- **Scope:** Hoàn thành `app.py`.

#### Commit 6: Phase 6 (Documentation & Finalization)
- **Message:** `docs(phase-6): finalize lab report, AI declaration, and screenshots`
- **Scope:** Hoàn thiện `README.md`, `AI_DECLARATION.md`.
