# app/scoring.py
import json
from .models import Response, Question, User

def calculate_relationship_report(room_id):
    """
    Analyzes live response matrices for a session and processes compatibility algorithms
    across explicit core psychological dimensions.
    """
    users = User.query.filter_by(room_id=room_id).all()
    if len(users) < 2:
        return None
        
    user_a, user_b = users[0], users[1]

    # Map database response arrays
    responses_a = {r.question_id: r.answer for r in Response.query.filter_by(user_id=user_a.id).all()}
    responses_b = {r.question_id: r.answer for r in Response.query.filter_by(user_id=user_b.id).all()}

    # Initialize data metrics matching our 4 core dimensions
    dimension_scores = {
        "Communication": {"total_points": 0, "max_points": 0},
        "Trust": {"total_points": 0, "max_points": 0},
        "Emotional Needs": {"total_points": 0, "max_points": 0},
        "Conflict Handling": {"total_points": 0, "max_points": 0}
    }
    
    prediction_matches = 0
    total_prediction_qs = 0

    common_question_ids = set(responses_a.keys()).intersection(set(responses_b.keys()))
    
    for q_id in common_question_ids:
        question = Question.query.get(q_id)
        dim = question.dimension if question.dimension in dimension_scores else "Communication"
        
        ans_a = responses_a[q_id]
        ans_b = responses_b[q_id]

        # Enforce aggressive timeout penalty
        if ans_a == "TIMEOUT" or ans_b == "TIMEOUT":
            dimension_scores[dim]["max_points"] += 10
            continue

        # TYPE 1: PREDICTION ALGORITHM
        if question.question_type == 'prediction':
            total_prediction_qs += 1
            dimension_scores[dim]["max_points"] += 10
            if ans_a == ans_b:
                dimension_scores[dim]["total_points"] += 10
                prediction_matches += 1
            else:
                dimension_scores[dim]["total_points"] += 2 # Partial empathy allowance

        # TYPE 2: STANDARD ALIGNMENT VALUE ALGORITHM
        else:
            dimension_scores[dim]["max_points"] += 10
            if ans_a == ans_b:
                dimension_scores[dim]["total_points"] += 10
            else:
                dimension_scores[dim]["total_points"] += 4 # Complementary offset values

    # Finalize percentage metrics safely
    final_dimensions = {}
    grand_total_points = 0
    grand_max_points = 0

    for dim, scores in dimension_scores.items():
        if scores["max_points"] > 0:
            pct = int((scores["total_points"] / scores["max_points"]) * 100)
            final_dimensions[dim] = min(pct, 100)
            grand_total_points += scores["total_points"]
            grand_max_points += scores["max_points"]
        else:
            final_dimensions[dim] = 0 # Cleaned placeholder: displays actual unreached data metric

    # Calculate exact mathematical compatibility score
    overall_score = int((grand_total_points / grand_max_points) * 100) if grand_max_points > 0 else 0

    # 6. Cleaned Relationship Suggestion Matrix
    # Derived purely from empirical calculations rather than hardcoded blocks
    suggested_dynamic = None
    if overall_score < 85:
        if final_dimensions.get("Communication", 0) >= 75:
            suggested_dynamic = "Best Friends Ecosystem"
        elif final_dimensions.get("Trust", 0) >= 75:
            suggested_dynamic = "Anchor Alignment"
        else:
            suggested_dynamic = "Evolving Growth Matrix"

    # 7. Personalized Feedback
    user_a_insights = {"name": user_a.name, "strengths": [], "advice": []}
    user_b_insights = {"name": user_b.name, "strengths": [], "advice": []}

    # User A Evaluation
    if final_dimensions.get("Communication", 0) >= 70:
        user_a_insights["strengths"].append("You articulate emotional boundaries cleanly without assigning blame.")
    else:
        user_a_insights["advice"].append("Practice active emotional expression; avoid withdrawing into silent processing frames.")

    if prediction_matches > (total_prediction_qs / 2):
        user_a_insights["strengths"].append("Exceptional emotional accuracy regarding your partner's internal motivators.")
    else:
        user_a_insights["advice"].append("Actively clarify intent before reacting to structural tonal patterns.")

    # User B Evaluation
    if final_dimensions.get("Emotional Needs", 0) >= 70:
        user_b_insights["strengths"].append("Highly responsive to subtle emotional bids and attachment calls.")
    else:
        user_b_insights["advice"].append("State emotional requirements explicitly; do not rely on implicit projection matching.")

    if final_dimensions.get("Trust", 0) >= 70:
        user_b_insights["strengths"].append("Maintains a highly transparent, non-defensive psychological foundation.")
    else:
        user_b_insights["advice"].append("Focus on creating shared psychological safety before initiating active troubleshooting loops.")

    # Structural Safety Check for Low Scoring Edge Cases
    if not user_a_insights["strengths"]:
        user_a_insights["strengths"].append("Shows a strong analytical commitment to confronting relationship data.")
    if not user_b_insights["strengths"]:
        user_b_insights["strengths"].append("Actively engaged in discovering core relational paradigms.")

    # 8. Pattern Extraction (Hidden Traits)
    hidden_traits = []
    if final_dimensions.get("Trust", 0) > 75 and final_dimensions.get("Communication", 0) < 60:
        hidden_traits.append("Implicit Citadel: High absolute trust, but vulnerable to heavy transmission blockages.")
    elif overall_score > 75 and prediction_matches == 0:
        hidden_traits.append("Spontaneous Alignment: Natural synergy present despite an inability to track intent metrics.")
    elif final_dimensions.get("Emotional Needs", 0) > 80 and final_dimensions.get("Conflict Handling", 0) < 60:
        hidden_traits.append("Passionate Volatility: Deep intrinsic affection patterns mixed with high conflict metrics.")
    elif overall_score < 50:
        # NEW: Catch brutal scores so it doesn't give them a false positive!
        hidden_traits.append("Friction Protocol: High emotional turbulence detected. Core realignment and communication overhaul required.")
    else:
        hidden_traits.append("Synchronous Harmony: Clean relational tracking with low psychological friction.")

    # 9. Chronological Heatmap Processing
    heatmap_data = []
    for q_id in common_question_ids:
        alignment = 1.0 if responses_a[q_id] == responses_b[q_id] else 0.25
        heatmap_data.append(alignment)

    # 10. Abstract Personality Summaries
    user_a_summary = f"{user_a.name} approaches attachment matrices via structured, internal processing pathways, placing high premiums on systemic security patterns."
    user_b_summary = f"{user_b.name} registers interpersonal shifts rapidly, prioritizing real-time clarity over long-term emotional containment structures."

    return {
        "overall_score": overall_score,
        "dimensions": final_dimensions,
        "suggested_dynamic": suggested_dynamic,
        "user_a_insights": user_a_insights,
        "user_b_insights": user_b_insights,
        "hidden_traits": hidden_traits,
        "heatmap_data": heatmap_data,
        "user_a_summary": user_a_summary,
        "user_b_summary": user_b_summary
    }