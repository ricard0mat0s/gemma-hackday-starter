"""Interface local: anotações → propostas → revisão humana → CSV."""

from pathlib import Path

import pandas as pd
import streamlit as st

from gemma_client import FIELDS, MAX_NOTES_LENGTH, TaskGenerationError, generate_tasks

LABELS = ("Título", "Descrição", "Responsável", "Prazo")


def tasks_to_csv(table: pd.DataFrame) -> bytes:
    # Evita interpretar texto como fórmula ao abrir o CSV em uma planilha.
    def safe_cell(value):
        text = "" if pd.isna(value) else str(value)
        return "'" + text if text.lstrip().startswith(("=", "+", "-", "@")) or text.startswith(("\t", "\r", "\n")) else text

    return table.map(safe_cell).to_csv(index=False).encode("utf-8-sig")


def load_example():
    st.session_state.notes = Path(__file__).with_name("examples").joinpath("notes.txt").read_text(encoding="utf-8")


def main():
    st.set_page_config(page_title="Das anotações às tarefas", page_icon="📝", layout="wide")
    st.title("Das anotações às tarefas")
    st.write("Use Gemma para propor tarefas. Revise cada proposta antes de assumir um compromisso.")
    st.caption("A interface roda no seu computador. Ao gerar, as anotações são enviadas à API do Google. Pratique com dados fictícios.")
    st.button("Carregar exemplo fictício", on_click=load_example)
    notes = st.text_area("Anotações da reunião ou do evento", key="notes", height=200, max_chars=MAX_NOTES_LENGTH)
    st.caption("Uma nova geração bem-sucedida substitui a tabela. Baixe o CSV antes se quiser guardar as edições.")
    if st.button("Gerar propostas de tarefas", type="primary"):
        try:
            with st.spinner("Gemma está lendo as anotações…"):
                tasks = generate_tasks(notes)
        except TaskGenerationError as error:
            st.error(str(error))
        else:
            old_version = st.session_state.get("table_version", 0)
            st.session_state.pop(f"editor_{old_version}", None)
            st.session_state.table_version = old_version + 1
            # A base fica fixa entre gerações: reaplicar os deltas do editor não
            # pode modificar a entrada e fazer edições anteriores desaparecerem.
            st.session_state.task_base = pd.DataFrame(tasks, columns=FIELDS).rename(columns=dict(zip(FIELDS, LABELS)))

    if "task_base" in st.session_state:
        st.subheader("Revise e edite")
        st.caption("Responsável ou prazo desconhecido fica vazio. Datas: AAAA-MM-DD. Confirme a célula com Enter ou clicando fora antes de baixar.")
        if st.session_state.task_base.empty:
            st.info("Nenhuma tarefa acionável foi encontrada. Você pode incluir uma linha manualmente.")
        edited = st.data_editor(
            st.session_state.task_base,
            key=f"editor_{st.session_state.table_version}",
            num_rows="dynamic",
            hide_index=True,
            width="stretch",
            column_config={label: st.column_config.TextColumn(label) for label in LABELS},
        )
        st.session_state.edited_tasks = edited.copy()
        st.download_button(
            "Baixar tarefas revisadas (CSV)",
            data=tasks_to_csv(edited),
            file_name="tarefas.csv",
            mime="text/csv",
            on_click="ignore",
        )
        st.caption("As edições ficam nesta sessão. Baixe o CSV antes de fechar ou recarregar a página. Textos que parecem fórmulas recebem um apóstrofo no CSV.")


if __name__ == "__main__":
    main()
