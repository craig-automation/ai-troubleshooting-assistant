import streamlit as st
from openai import OpenAI

st.title("AI Incident Assistant")
st.caption("AI-powered incident analysis based on engineering reasoning patterns")

incident = st.text_area("Describe the incident")

if st.button("Analyse Incident"):
    if not incident.strip():
        st.warning("Please enter an incident description")
    else:
        try:
            with st.spinner("Analysing incident..."):
                client = OpenAI()

                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an engineering diagnostics assistant. "
                                "Analyse the incident and respond in exactly this format:\n\n"
                                "Likely Cause: <text>\n"
                                "Severity: <Low/Medium/High>\n"
                                "Recommended Actions:\n"
                                "- <action 1>\n"
                                "- <action 2>\n"
                                "- <action 3>"
                            )
                        },
                        {
                            "role": "user",
                            "content": incident
                        }
                    ]
                )

            output = response.choices[0].message.content

            likely_cause = ""
            severity = ""
            actions = []

            for line in output.split("\n"):
                line = line.strip()

                if line.startswith("Likely Cause:"):
                    likely_cause = line.replace("Likely Cause:", "").strip()
                elif line.startswith("Severity:"):
                    severity = line.replace("Severity:", "").strip()
                elif line.startswith("-"):
                    actions.append(line.replace("-", "", 1).strip())

            st.subheader("Analysis")

            st.write("**Likely Cause:**")
            st.write(likely_cause if likely_cause else "No cause returned")

            st.write("**Severity:**")
            st.write(severity if severity else "No severity returned")

            st.write("**Recommended Actions:**")
            if actions:
                for i, action in enumerate(actions, 1):
                    st.write(f"{i}. {action}")
            else:
                st.write("No actions returned")

        except Exception as e:
            st.error(f"Error: {e}")
