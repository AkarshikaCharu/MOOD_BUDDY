import streamlit as st
import styles, analysis, database as db, auth, time

def main():
    st.set_page_config(page_title="Mood Buddy", layout="wide")
    styles.apply_styles()
    db.init_db()

    if 'page' not in st.session_state: st.session_state.page = "Landing"
    if 'messages' not in st.session_state: st.session_state.messages = []
    if 'greeted' not in st.session_state: st.session_state.greeted = False
    if 'show_analysis' not in st.session_state: st.session_state.show_analysis = False

    # --- TOP NAVIGATION BAR ---
    nav_html = f"""
        <div class="custom-nav">
            <div style="font-size: 1.6rem; font-weight: bold;">💜 Mood Buddy</div>
            <div style="display: flex; gap: 25px; align-items: center;">
                <span>{st.session_state.user if st.session_state.get('logged_in') else ""}</span>
            </div>
        </div>
    """
    st.markdown(nav_html, unsafe_allow_html=True)
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    # 1. LANDING
    # 1. LANDING PAGE
    if st.session_state.page == "Landing":
        st.markdown("<h1 style='text-align: center; color: #4B0082;'>💜 Mood Buddy</h1>", unsafe_allow_html=True)

        st.markdown("""
                <div style="background-color: white; padding: 30px; border-radius: 20px; border: 1px solid #9370DB;">
                    <p style="color: black; font-size: 1.2rem; line-height: 1.6; text-align: center;">
                        <b>Welcome to Mood Buddy—your digital sanctuary for the days that feel a little too heavy.</b><br><br>
                        We believe that everyone deserves a space to be heard without being judged, managed, or "fixed." 
                        Unlike typical bots, Mood Buddy doesn’t interrogate you with clinical questions or overwhelm you with 
                        generic advice. We are here to sit with you in the quiet, validate your feelings, and offer a soft 
                        place to land.<br><br>
                        Whether you’re bone-tired from work, feeling a flicker of joy, or just need to vent into the void, 
                        your words are safe here. No complex APIs, no data sharing—just a gentle, private conversation 
                        between friends. Step inside, take a deep breath, and tell us: 
                        <b>how is your soul feeling today?</b>
                    </p>
                </div>
            """, unsafe_allow_html=True)

        st.write("---")
        col1, col2 = st.columns(2)
        if col1.button("Enter Our Space (Login)"):
            st.session_state.page = "Login"
            st.rerun()
        if col2.button("Join the Sanctuary (Sign Up)"):
            st.session_state.page = "SignUp"
            st.rerun()
    # 2. SIGN UP
    elif st.session_state.page == "SignUp":
        st.subheader("Join our space")
        u = st.text_input("Choose Username")
        p = st.text_input("Choose Password", type="password")
        if st.button("Create Account"):
            db.add_user(u, auth.make_hashes(p))
            st.success("Account created! Redirecting...")
            time.sleep(1); st.session_state.page = "Login"; st.rerun()

    # 3. LOGIN
    elif st.session_state.page == "Login":
        st.subheader("Welcome Back")
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("Login"):
            if db.login_user(u, auth.make_hashes(p)):
                st.session_state.logged_in = True
                st.session_state.user = u
                st.session_state.page = "Chat"; st.rerun()

    # 4. CHAT PAGE
    elif st.session_state.page == "Chat":
        # Navigation Actions
        cols = st.columns([5, 1, 1.5, 1])
        if cols[1].button("Chat"): st.session_state.show_analysis = False; st.rerun()
        if cols[2].button("Analysis"): st.session_state.show_analysis = True; st.rerun()
        if cols[3].button("Logout"): 
            st.session_state.logged_in = False
            st.session_state.page = "Landing"; st.rerun()

        if st.session_state.show_analysis:
            # Show the Mood Report
            report = analysis.get_mood_analysis(st.session_state.messages)
            st.markdown(f"<div style='background: white; padding: 30px; border-radius: 20px; color: black;'>{report}</div>", unsafe_allow_html=True)
        else:
            # Handle Start Greeting
            if not st.session_state.greeted:
                st.session_state.messages.append({"role": "assistant", "content": analysis.get_greeting(st.session_state.user)})
                st.session_state.greeted = True

            # Display Chat
            for msg in st.session_state.messages:
                with st.chat_message(msg["role"]): st.write(msg["content"])

            if prompt := st.chat_input("Tell me what's on your mind..."):
                st.session_state.messages.append({"role": "user", "content": prompt})
                st.rerun()

            # Generate response if last msg is from user
            if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
                reply = analysis.get_static_response(st.session_state.messages[-1]["content"])
                st.session_state.messages.append({"role": "assistant", "content": reply})
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()