import streamlit as st

from services.auth import current_user, get_role, sign_out


def _handle_logout():
    sign_out()


def render_sidebar():
    with st.sidebar:
        st.title("Clustering and panel regression")

        st.divider()

        if get_role() == "admin":
            st.page_link(
                "pages/use_count.py",
                label="Jumlah penggunaan layanan",
                icon="📊",
            )
            st.page_link(
                "pages/user_count.py",
                label="Jumlah registrasi pengguna",
                icon="👥",
            )
        else:
            st.page_link(
                "pages/clustering.py",
                label="Clustering",
                icon="📊",
            )
            st.page_link(
                "pages/panel_regression.py",
                label="Panel Regression",
                icon="📈",
            )


        st.divider()

        user = current_user()
        if user is not None:
            st.caption(f"Logged in as {user.email}")
        st.button("Logout", icon="🚪", on_click=_handle_logout)
        st.divider()

        if get_role()=="admin":
            st.link_button(
                "Lihat masukan pengguna",
                url="https://docs.google.com/spreadsheets/d/13vVQ56RuwNWsGZGAycWioF1sKDjQofXklZuWXujvpV0/edit?usp=sharing",
                icon="📋"
            )
        else:
            st.link_button(
                "Give us your opinion",
                url="https://docs.google.com/forms/d/e/1FAIpQLScx0c3dJIJMMjHX8SOp4dpKDdsznHXLoLRyCW4OSvJnz2vXCg/viewform?usp=dialog",
                icon="📢"
            )
        st.caption("Contact developer: jervishuang123@gmail.com")