import streamlit as st

def apply_modern_styles():
    """Apply modern styles by loading the CSS file"""
    # Styles are now loaded from style.css in app.py
    pass

def page_header(title, subtitle=None):
    """Render a consistent page header"""
    st.markdown(
        f'''
        <div class="page-header">
            <h1 class="header-title">{title}</h1>
            {f'<p class="header-subtitle">{subtitle}</p>' if subtitle else ''}
        </div>
        ''',
        unsafe_allow_html=True
    )

def hero_section(title, subtitle=None, description=None):
    """Render a clean minimal hero section"""
    if description and not subtitle:
        subtitle = description
        description = None
    
    st.markdown(
        f'''
        <div class="page-hero">
            <h1>{title}</h1>
            {f'<p>{subtitle}</p>' if subtitle else ''}
            {f'<p>{description}</p>' if description else ''}
        </div>
        ''',
        unsafe_allow_html=True
    )

def feature_card(icon, title, description):
    """Render a clean feature card"""
    st.markdown(f"""
        <div class="feature-card">
            <i class="{icon} feature-icon"></i>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)

def metric_card(label, value, delta=None, icon=None):
    """Render a metric card"""
    icon_html = f'<i class="{icon}"></i>' if icon else ''
    delta_html = f'<div class="metric-delta">{delta}</div>' if delta else ''
    
    st.markdown(f"""
        <div class="metric-card">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                <div class="metric-label">{label}</div>
                <div style="color: var(--accent); font-size: 16px;">{icon_html}</div>
            </div>
            <div class="metric-value">{value}</div>
            {delta_html}
        </div>
    """, unsafe_allow_html=True)

def template_card(title, description, image_url=None):
    """Render a clean template card"""
    image_html = f'<img src="{image_url}" style="width: 100%; border-radius: 6px; margin-bottom: 12px; border: 1px solid var(--border);" />' if image_url else ''
    
    st.markdown(f"""
        <div class="template-preview">
            {image_html}
            <h3 style="margin-bottom: 4px; font-size: 16px;">{title}</h3>
            <p style="margin: 0; font-size: 13px; color: var(--text-secondary);">{description}</p>
        </div>
    """, unsafe_allow_html=True)

def feedback_card(name, feedback, rating):
    """Render a feedback card"""
    stars = "⭐" * int(rating)
    
    st.markdown(f"""
        <div class="feedback-card">
            <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
                <div style="font-weight: 600; font-size: 14px; color: var(--text-primary);">{name}</div>
                <div style="font-size: 12px;">{stars}</div>
            </div>
            <p style="margin: 0; font-size: 14px; color: var(--text-secondary);">{feedback}</p>
        </div>
    """, unsafe_allow_html=True)

def alert(message, type="info"):
    """Display a clean alert message"""
    alert_types = {
        "info": ("ℹ️", "stInfo"),
        "success": ("✅", "stSuccess"),
        "warning": ("⚠️", "stWarning"),
        "error": ("❌", "stError")
    }
    icon, alert_class = alert_types.get(type, alert_types["info"])
    
    st.markdown(f"""
        <div class="{alert_class}" style="display:flex; align-items:flex-start; gap:8px;">
            <span>{icon}</span>
            <span style="font-weight: 500;">{message}</span>
        </div>
    """, unsafe_allow_html=True)

def render_feedback(feedback_data):
    """Render feedback results"""
    if not feedback_data:
        return
    
    feedback_html = """
    <div class="card" style="margin-top: 24px;">
        <h3 style="margin-top:0;">Resume Analysis Feedback</h3>
        <div style="display:flex; flex-direction:column; gap:16px; margin-top:16px;">
    """
    
    for category, items in feedback_data.items():
        if items:
            for item in items:
                feedback_html += f"""
                <div style="background: var(--bg-hover); padding: 12px; border-radius: 6px; border-left: 3px solid var(--accent);">
                    <div style="font-weight:600; font-size:13px; color:var(--text-primary); text-transform:uppercase; margin-bottom:4px;">{category}</div>
                    <div style="font-size:14px; color:var(--text-secondary);">{item}</div>
                </div>
                """
    
    feedback_html += """
        </div>
    </div>
    """
    
    st.markdown(feedback_html, unsafe_allow_html=True)

def render_analytics_section(resume_uploaded=False, metrics=None):
    """Render the analytics section of the dashboard"""
    if not metrics:
        metrics = {'views': 0, 'downloads': 0, 'score': 'N/A'}
    
    st.markdown(f"""
        <div class="metric-card">
            <div style="display: flex; align-items: center; margin-bottom: 12px; color: var(--accent);">
                <i class="fas fa-eye" style="font-size: 20px; margin-right: 12px;"></i>
                <h3 style="margin: 0; font-size: 15px;">Resume Views</h3>
            </div>
            <div class="metric-value">{metrics['views']}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="metric-card" style="margin-top: 16px;">
            <div style="display: flex; align-items: center; margin-bottom: 12px; color: var(--accent);">
                <i class="fas fa-download" style="font-size: 20px; margin-right: 12px;"></i>
                <h3 style="margin: 0; font-size: 15px;">Downloads</h3>
            </div>
            <div class="metric-value">{metrics['downloads']}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="metric-card" style="margin-top: 16px;">
            <div style="display: flex; align-items: center; margin-bottom: 12px; color: var(--accent);">
                <i class="fas fa-chart-line" style="font-size: 20px; margin-right: 12px;"></i>
                <h3 style="margin: 0; font-size: 15px;">Profile Score</h3>
            </div>
            <div class="metric-value">{metrics['score']}</div>
        </div>
    """, unsafe_allow_html=True)

def render_activity_section(resume_uploaded=False):
    """Render the recent activity section"""
    st.markdown("""
        <div class="card" style="height: 100%;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px; border-bottom: 1px solid var(--border); padding-bottom: 12px;">
                <i class="fas fa-history" style="color: var(--accent); font-size: 18px;"></i>
                <h2 style="margin: 0; font-size: 18px;">Recent Activity</h2>
            </div>
    """, unsafe_allow_html=True)
    
    if resume_uploaded:
        st.markdown("""
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div style="display: flex; align-items: center; gap: 12px; font-size: 14px; color: var(--text-secondary);">
                    <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--success);"></div>
                    Resume uploaded and analyzed
                </div>
                <div style="display: flex; align-items: center; gap: 12px; font-size: 14px; color: var(--text-secondary);">
                    <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--info);"></div>
                    Generated optimization suggestions
                </div>
                <div style="display: flex; align-items: center; gap: 12px; font-size: 14px; color: var(--text-secondary);">
                    <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--warning);"></div>
                    Updated profile score
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="empty-state">
                <i class="fas fa-upload"></i>
                <p>Upload your resume to see activity</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def render_suggestions_section(resume_uploaded=False):
    """Render the suggestions section"""
    st.markdown("""
        <div class="card" style="height: 100%;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px; border-bottom: 1px solid var(--border); padding-bottom: 12px;">
                <i class="fas fa-lightbulb" style="color: var(--accent); font-size: 18px;"></i>
                <h2 style="margin: 0; font-size: 18px;">Suggestions</h2>
            </div>
    """, unsafe_allow_html=True)
    
    if resume_uploaded:
        st.markdown("""
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div style="background: var(--bg-hover); padding: 12px; border-radius: 6px; font-size: 13px; color: var(--text-secondary);">
                    <strong style="color: var(--text-primary); display:block; margin-bottom:4px;">Quantifiable Achievements</strong>
                    Add more numbers and metrics to your experience section.
                </div>
                <div style="background: var(--bg-hover); padding: 12px; border-radius: 6px; font-size: 13px; color: var(--text-secondary);">
                    <strong style="color: var(--text-primary); display:block; margin-bottom:4px;">Keyword Optimization</strong>
                    Include more relevant keywords for your target role.
                </div>
                <div style="background: var(--bg-hover); padding: 12px; border-radius: 6px; font-size: 13px; color: var(--text-secondary);">
                    <strong style="color: var(--text-primary); display:block; margin-bottom:4px;">Formatting</strong>
                    Ensure your resume format is ATS-friendly.
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="empty-state">
                <i class="fas fa-file-alt"></i>
                <p>Upload your resume to get suggestions</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)