#############################
# CROP RECOMMENDATION LOGIC
#############################

def get_crop_candidates(soil_type, ph, temp, rainfall, n, season):
    soil_type = soil_type.lower()
    season = season.lower()
    
    crops_db = [
        {"name": "Rice (Paddy)", "img": "https://loremflickr.com/320/320/rice,plantation/all", "soil": "clay loamy loam", "ph_min": 5.5, "ph_max": 7, "n_min": 50, "n_max": 100, "rain_min": 1000, "rain_max": 2000, "temp_min": 20, "temp_max": 30, "season": "kharif"},
        {"name": "Wheat", "img": "https://loremflickr.com/320/320/wheat,field/all", "soil": "loamy loam", "ph_min": 6, "ph_max": 7.5, "n_min": 80, "n_max": 120, "rain_min": 500, "rain_max": 800, "temp_min": 15, "temp_max": 25, "season": "rabi"},
        {"name": "Maize (Corn)", "img": "https://loremflickr.com/320/320/maize,corn/all", "soil": "loamy loam", "ph_min": 5.5, "ph_max": 7.5, "n_min": 60, "n_max": 120, "rain_min": 500, "rain_max": 800, "temp_min": 18, "temp_max": 27, "season": "kharif rabi"},
        {"name": "Soybean", "img": "https://loremflickr.com/320/320/soybean,plant/all", "soil": "loamy loam", "ph_min": 6, "ph_max": 7.5, "n_min": 20, "n_max": 40, "rain_min": 600, "rain_max": 1000, "temp_min": 20, "temp_max": 30, "season": "kharif"},
        {"name": "Cotton", "img": "https://loremflickr.com/320/320/cotton,plant/all", "soil": "black loamy loam", "ph_min": 6, "ph_max": 8, "n_min": 80, "n_max": 120, "rain_min": 600, "rain_max": 1200, "temp_min": 21, "temp_max": 30, "season": "kharif"},
        {"name": "Sugarcane", "img": "https://loremflickr.com/320/320/sugarcane,plantation/all", "soil": "loamy loam", "ph_min": 6, "ph_max": 7.5, "n_min": 100, "n_max": 150, "rain_min": 1000, "rain_max": 1500, "temp_min": 20, "temp_max": 30, "season": "annual"},
        {"name": "Groundnut", "img": "https://loremflickr.com/320/320/peanut,plant/all", "soil": "sandy loamy loam", "ph_min": 5.5, "ph_max": 7, "n_min": 20, "n_max": 40, "rain_min": 500, "rain_max": 1000, "temp_min": 20, "temp_max": 30, "season": "kharif"},
        {"name": "Mustard", "img": "https://loremflickr.com/320/320/mustard,field/all", "soil": "loamy loam", "ph_min": 6, "ph_max": 7.5, "n_min": 40, "n_max": 80, "rain_min": 400, "rain_max": 600, "temp_min": 10, "temp_max": 25, "season": "rabi"},
        {"name": "Potato", "img": "https://loremflickr.com/320/320/potato,plant/all", "soil": "sandy loamy loam", "ph_min": 5, "ph_max": 6.5, "n_min": 100, "n_max": 150, "rain_min": 500, "rain_max": 700, "temp_min": 15, "temp_max": 20, "season": "rabi"},
        {"name": "Tomato", "img": "https://loremflickr.com/320/320/tomato,plant/all", "soil": "loamy loam", "ph_min": 6, "ph_max": 7.5, "n_min": 80, "n_max": 120, "rain_min": 600, "rain_max": 800, "temp_min": 20, "temp_max": 30, "season": "all annual"},
        {"name": "Onion", "img": "https://loremflickr.com/320/320/onion,plant/all", "soil": "loamy loam", "ph_min": 6, "ph_max": 7.5, "n_min": 80, "n_max": 120, "rain_min": 500, "rain_max": 700, "temp_min": 20, "temp_max": 30, "season": "rabi"},
        {"name": "Barley", "img": "https://loremflickr.com/320/320/barley,field/all", "soil": "loamy loam", "ph_min": 6, "ph_max": 7.5, "n_min": 60, "n_max": 100, "rain_min": 400, "rain_max": 600, "temp_min": 12, "temp_max": 25, "season": "rabi"},
        {"name": "Millet", "img": "https://loremflickr.com/320/320/millet,plant/all", "soil": "sandy", "ph_min": 5, "ph_max": 6.5, "n_min": 40, "n_max": 80, "rain_min": 300, "rain_max": 600, "temp_min": 25, "temp_max": 35, "season": "kharif"},
        {"name": "Sorghum", "img": "https://loremflickr.com/320/320/sorghum,plant/all", "soil": "sandy loamy loam", "ph_min": 5.5, "ph_max": 7.5, "n_min": 50, "n_max": 100, "rain_min": 400, "rain_max": 800, "temp_min": 25, "temp_max": 35, "season": "kharif"},
        {"name": "Chickpea", "img": "https://loremflickr.com/320/320/chickpea,plant/all", "soil": "loamy loam", "ph_min": 6, "ph_max": 7.5, "n_min": 20, "n_max": 40, "rain_min": 400, "rain_max": 600, "temp_min": 18, "temp_max": 30, "season": "rabi"}
    ]
    
    for c in crops_db:
        score = 0
        reasons = []
        
        # Season Match - 25%
        if season in c['season'].lower():
            score += 25
            reasons.append(f"Ideal for {season.capitalize()} season.")
        else:
            reasons.append(f"Usually grown in {c['season'].capitalize()} season.")
            
        # Soil Match - 25%
        # Check intersection of user soil types and crop suitable soil types
        input_soils = set(soil_type.replace(',', ' ').split())
        crop_soils = set(c['soil'].split())
        if input_soils.intersection(crop_soils) or not input_soils:
            score += 25
            reasons.append("Grows wonderfully in your exact soil type.")
        else:
            reasons.append(f"Best suited for {c['soil'].replace(' ', '/')} soil.")
            
        # Temperature Match - 15%
        if c['temp_min'] <= temp <= c['temp_max']:
            score += 15
            reasons.append("Temperatures in your area are perfectly suited.")
        else:
            reasons.append(f"Prefers temp between {c['temp_min']}-{c['temp_max']}°C.")
            
        # Rainfall Match - 15%
        if c['rain_min'] <= rainfall <= c['rain_max']:
            score += 15
            reasons.append("Receives the optimal amount of rainfall natively.")
        else:
            reasons.append(f"Requires rainfall between {c['rain_min']}-{c['rain_max']}mm.")
            
        # N & pH Match - 20%
        if c['n_min'] <= n <= c['n_max'] and c['ph_min'] <= ph <= c['ph_max']:
            score += 20
            reasons.append("Soil pH and Nitrogen levels are perfect natively.")
        else:
            reasons.append("May require slight pH balancing or specific NPK management.")
            
        c['score'] = score
        c['desc'] = " ".join(reasons)
        
        # Star ratings
        if score >= 90:
            c['stars'] = "⭐⭐⭐⭐⭐ (Very High)"
        elif score >= 75:
            c['stars'] = "⭐⭐⭐⭐ (High)"
        elif score >= 60:
            c['stars'] = "⭐⭐⭐ (Moderate)"
        else:
            c['stars'] = "⭐⭐ (Low)"
            
    crops_db.sort(key=lambda x: x['score'], reverse=True)
    return crops_db[:4]


def predict_crop(soil_type, ph, temp, rainfall, humidity, n, p, k, location, season):
    
    # 1. Provide interpretation mapping
    html = f"""
    <div style="font-family:'Inter', sans-serif; color:#cbd5e1; line-height:1.6; margin-top:1rem;">
        <p style="margin-bottom:1.5rem;">Based on the values you provided, we can recommend suitable crops scientifically. I'll interpret your inputs first, then suggest crops that match those conditions.</p>
        
        <h3 style="color:#34d399; margin-bottom:0.75rem; font-size:1.1rem; border-bottom:1px solid rgba(52,211,153,0.2); padding-bottom:0.5rem;">Given Input Conditions & Interpretation</h3>
        <div style="overflow-x:auto; margin-bottom:1.5rem;">
            <table style="width:100%; text-align:left; border-collapse:collapse; background:rgba(15,23,42,0.4); border-radius:8px; overflow:hidden;">
                <thead>
                    <tr style="background:rgba(52,211,153,0.1); color:#34d399;">
                        <th style="padding:0.75rem 1rem;">Factor</th>
                        <th style="padding:0.75rem 1rem;">Value</th>
                        <th style="padding:0.75rem 1rem;">Interpretation</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:0.75rem 1rem;">Soil Type</td><td style="padding:0.75rem 1rem; color:#fff;">{soil_type}</td><td style="padding:0.75rem 1rem; color:#fff;">Important structural baseline</td></tr>
                    <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:0.75rem 1rem;">Soil pH</td><td style="padding:0.75rem 1rem; color:#fff;">{ph}</td><td style="padding:0.75rem 1rem; color:#fff;">Standard baseline</td></tr>
                    <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:0.75rem 1rem;">Temperature</td><td style="padding:0.75rem 1rem; color:#fff;">{temp}°C</td><td style="padding:0.75rem 1rem; color:#fff;">Current local average</td></tr>
                    <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:0.75rem 1rem;">Rainfall</td><td style="padding:0.75rem 1rem; color:#fff;">{rainfall} mm</td><td style="padding:0.75rem 1rem; color:#fff;">Determines irrigation needs</td></tr>
                    <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:0.75rem 1rem;">Humidity</td><td style="padding:0.75rem 1rem; color:#fff;">{humidity}%</td><td style="padding:0.75rem 1rem; color:#fff;">Affects transpiration rates</td></tr>
                    <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:0.75rem 1rem;">Nitrogen (N)</td><td style="padding:0.75rem 1rem; color:#fff;">{n} kg/ha</td><td style="padding:0.75rem 1rem; color:#fff;">Essential macronutrient</td></tr>
                    <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:0.75rem 1rem;">Season</td><td style="padding:0.75rem 1rem; color:#fff; text-transform:capitalize;">{season}</td><td style="padding:0.75rem 1rem; color:#fff;">Defines growth cycle length</td></tr>
                </tbody>
            </table>
        </div>
        
        <p style="background:rgba(59,130,246,0.1); border-left:4px solid #3b82f6; padding:1rem; border-radius:4px; margin-bottom:2rem;">
            <strong>Conclusion:</strong> These are solid generic farming conditions. We matched your inputs against the minimum and maximum ranges spanning 15 major crops to determine the optimal choices below!
        </p>
        
        <h3 style="color:#34d399; margin-bottom:1rem; font-size:1.1rem; border-bottom:1px solid rgba(52,211,153,0.2); padding-bottom:0.5rem;">Recommended Crops for Your Conditions</h3>
    """
    
    # 2. Get 4 crop candidates
    candidates = get_crop_candidates(soil_type, float(ph), float(temp), float(rainfall), float(n), season)
    
    for idx, crop in enumerate(candidates):
        html += f"""
        <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.06); border-radius:12px; padding:1.25rem; margin-bottom:1.25rem; display:flex; gap:1.5rem; align-items:flex-start;">
            
            <div style="flex-shrink:0;">
                <div style="width:80px; height:80px; background:linear-gradient(135deg, rgba(52,211,153,0.2), rgba(59,130,246,0.2)); border-radius:16px; overflow:hidden; display:flex; align-items:center; justify-content:center; box-shadow:0 8px 16px rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.1);">
                    <img src="{crop['img']}" alt="{crop['name']}" style="width:100%; height:100%; object-fit:cover;" onerror="this.style.display='none'">
                </div>
            </div>
            
            <div>
                <h4 style="color:#fff; font-size:1.1rem; margin-bottom:0.5rem;">
                    {idx+1}) {crop['name']} 
                    { " — Best Match" if idx == 0 else "" }
                </h4>
                <p style="font-size:0.85rem; color:#94a3b8; margin-bottom:0.5rem;"><strong>Why {crop['name'].split(' ')[0]} is suitable:</strong><br/>{crop['desc']}</p>
                <p style="font-size:0.9rem; margin:0;"><strong style="color:#3b82f6;">Suitability:</strong> {crop['stars']}</p>
            </div>
        </div>
        """
        
    # 3. Final summary
    summary_list = "".join([f"<li style='margin-bottom:0.25rem;'>{c['name']} {('— Most suitable' if i==0 else '')}</li>" for i, c in enumerate(candidates)])
    
    html += f"""
        <h3 style="color:#34d399; margin-top:2rem; margin-bottom:0.75rem; font-size:1.1rem;">Final Recommendation (Top Choices)</h3>
        <div style="background:rgba(15,23,42,0.4); padding:1rem 1.5rem; border-radius:8px; border:1px solid rgba(255,255,255,0.05);">
            <ul style="margin:0; padding-left:1rem; color:#fff;">
                {summary_list}
            </ul>
        </div>
    </div>
    """
    
    return html


def predict_fertilizer(crop_type, location, soil_type, ph, n, p, k, area, stage, previous_fert="", irrigation=""):
    stage = stage.lower()
    
    # 1. Analyze NPK Levels 
    n_status = "Optimal"
    p_status = "Optimal"
    k_status = "Optimal"
    
    if n < 50: n_status = "Low"
    elif n > 120: n_status = "High"
    
    if p < 30: p_status = "Low"
    elif p > 70: p_status = "High"
    
    if k < 40: k_status = "Low"
    elif k > 80: k_status = "High"

    # Analyze pH
    ph_status = "Optimal"
    if ph < 6.0: ph_status = "Acidic (May need lime)"
    elif 6.0 <= ph <= 7.5: ph_status = "Ideal for most crops"
    else: ph_status = "Alkaline (May need sulfur)"

    # Base Rates (Per Acre) based on dataset
    urea_base = 50
    dap_base = 25
    mop_base = 20
    
    # Adjust based on stage
    primary_need = "Nitrogen"
    if 'vegetative' in stage:
        primary_need = "Nitrogen"
        urea_base += 10
    elif 'flowering' in stage or 'fruiting' in stage:
        primary_need = "Potassium & Phosphorus"
        urea_base -= 20
        mop_base += 10
    elif 'seeding' in stage:
        primary_need = "Phosphorus"
        dap_base += 10
        
    # HTML Formatting exactly to exam-style specs
    html_output = f"""
    <div style="font-family:'Inter', sans-serif; color:#cbd5e1; line-height:1.6; margin-top:1rem;">
        
        <h3 style="color:#60a5fa; margin-bottom:1.5rem; font-size:1.2rem; border-bottom:1px solid rgba(96,165,250,0.2); padding-bottom:0.5rem;">
            🌾 Recommended Fertilizer Plan for {crop_type.capitalize()} 
            <span style="font-size:0.9rem; color:#94a3b8; font-weight:normal;">({location if location else 'Local'}, {soil_type.capitalize()} Soil)</span>
        </h3>
        
        <!-- Section 1 -->
        <h4 style="color:#e2e8f0; font-size:1.05rem; margin-bottom:0.5rem;">1) Soil Condition Summary</h4>
        <div style="background:rgba(255,255,255,0.02); padding:1rem; border-radius:8px; margin-bottom:1.5rem; border:1px solid rgba(255,255,255,0.05);">
            <ul style="margin:0; padding-left:1.5rem;">
                <li style="margin-bottom:0.25rem;"><strong>Soil pH:</strong> {ph} &rarr; <span style="color:{'#f87171' if 'Acidic' in ph_status or 'Alkaline' in ph_status else '#34d399'};">{ph_status}</span></li>
                <li style="margin-bottom:0.25rem;"><strong>Nitrogen ({n} kg/ha):</strong> <span style="color:{'#f87171' if n_status != 'Optimal' else '#34d399'};">{n_status}</span></li>
                <li style="margin-bottom:0.25rem;"><strong>Phosphorus ({p} kg/ha):</strong> <span style="color:{'#f87171' if p_status != 'Optimal' else '#34d399'};">{p_status}</span></li>
                <li style="margin-bottom:0.25rem;"><strong>Potassium ({k} kg/ha):</strong> <span style="color:{'#f87171' if k_status != 'Optimal' else '#34d399'};">{k_status}</span></li>
                <li style="margin-bottom:0.25rem;"><strong>Growth stage:</strong> {stage.capitalize()} (needs more {primary_need})</li>
            </ul>
            <p style="margin:1rem 0 0 0; color:#cbd5e1; background:rgba(59,130,246,0.1); padding:0.75rem; border-left:3px solid #3b82f6; border-radius:4px;">
                👉 <strong>Therefore:</strong> The crop mainly needs {primary_need} fertilizer now, balanced with standard NPK doses.
            </p>
        </div>

        <!-- Section 2 -->
        <h4 style="color:#e2e8f0; font-size:1.05rem; margin-bottom:0.75rem;">2) Recommended Fertilizers and Quantity (Per Acre)</h4>
        
        <div style="display:flex; flex-direction:column; gap:1rem; margin-bottom:1.5rem;">
            <div style="background:rgba(15,23,42,0.4); padding:1rem; border-radius:8px; border:1px solid rgba(255,255,255,0.05);">
                <h5 style="margin:0 0 0.5rem 0; color:#34d399; font-size:1rem;">🌱 Urea (Nitrogen Source)</h5>
                <p style="margin:0 0 0.25rem 0;"><strong>Recommended Dose:</strong> {urea_base} kg per acre</p>
                <p style="margin:0; font-size:0.9rem; color:#94a3b8;"><strong>Purpose:</strong> Promotes leaf growth, increases tillering, improves plant height.</p>
            </div>
            
            <div style="background:rgba(15,23,42,0.4); padding:1rem; border-radius:8px; border:1px solid rgba(255,255,255,0.05);">
                <h5 style="margin:0 0 0.5rem 0; color:#34d399; font-size:1rem;">🌾 DAP (Phosphorus Source)</h5>
                <p style="margin:0 0 0.25rem 0;"><strong>Recommended Dose:</strong> {dap_base} kg per acre</p>
                <p style="margin:0; font-size:0.9rem; color:#94a3b8;"><strong>Purpose:</strong> Strong root development, early plant growth, better nutrient absorption.</p>
            </div>
            
            <div style="background:rgba(15,23,42,0.4); padding:1rem; border-radius:8px; border:1px solid rgba(255,255,255,0.05);">
                <h5 style="margin:0 0 0.5rem 0; color:#34d399; font-size:1rem;">🌿 MOP (Potash / Potassium)</h5>
                <p style="margin:0 0 0.25rem 0;"><strong>Recommended Dose:</strong> {mop_base} kg per acre</p>
                <p style="margin:0; font-size:0.9rem; color:#94a3b8;"><strong>Purpose:</strong> Improves disease resistance, strengthens stems, increases grain filling later.</p>
            </div>
        </div>

        <!-- Section 3 -->
        <h4 style="color:#e2e8f0; font-size:1.05rem; margin-bottom:0.75rem;">3) Total Fertilizer Requirement for Your Land ({area} Acres)</h4>
        <table style="width:100%; text-align:left; border-collapse:collapse; background:rgba(255,255,255,0.02); margin-bottom:1.5rem; border-radius:8px; overflow:hidden;">
            <thead>
                <tr style="background:rgba(59,130,246,0.1); color:#60a5fa;">
                    <th style="padding:0.75rem;">Fertilizer</th>
                    <th style="padding:0.75rem;">Per Acre</th>
                    <th style="padding:0.75rem;">For {area} Acres</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.75rem;">Urea</td>
                    <td style="padding:0.75rem;">{urea_base} kg</td>
                    <td style="padding:0.75rem; font-weight:bold; color:#fff;">{int(urea_base * area)} kg</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.75rem;">DAP</td>
                    <td style="padding:0.75rem;">{dap_base} kg</td>
                    <td style="padding:0.75rem; font-weight:bold; color:#fff;">{int(dap_base * area)} kg</td>
                </tr>
                <tr>
                    <td style="padding:0.75rem;">MOP</td>
                    <td style="padding:0.75rem;">{mop_base} kg</td>
                    <td style="padding:0.75rem; font-weight:bold; color:#fff;">{int(mop_base * area)} kg</td>
                </tr>
            </tbody>
        </table>

        <!-- Section 4 -->
        <h4 style="color:#e2e8f0; font-size:1.05rem; margin-bottom:0.5rem;">4) Application Schedule (Important)</h4>
        <div style="background:rgba(255,255,255,0.02); padding:1rem; border-radius:8px; margin-bottom:1.5rem; border:1px solid rgba(255,255,255,0.05);">
            <p style="margin:0 0 0.5rem 0;"><strong>Now ({stage.capitalize()}):</strong></p>
            <ul style="margin:0 0 1rem 0; padding-left:1.5rem;">
                <li>Apply 50% Urea + Full DAP + Full MOP</li>
            </ul>
            <p style="margin:0 0 0.5rem 0;"><strong>After 20–25 days:</strong></p>
            <ul style="margin:0 0 1rem 0; padding-left:1.5rem;">
                <li>Apply remaining 50% Urea</li>
            </ul>
            <p style="margin:0; font-size:0.9rem; color:#94a3b8;">This method is called split application, and it reduces nitrogen loss, improves yield, and saves fertilizer cost.</p>
        </div>

        <!-- Section 5 -->
        <h4 style="color:#e2e8f0; font-size:1.05rem; margin-bottom:0.5rem;">5) Extra Practical Tips for Your Situation ({location if location else 'Local'}, {soil_type.capitalize()} Soil)</h4>
        <div style="background:rgba(255,255,255,0.02); padding:1rem; border-radius:8px; border:1px solid rgba(255,255,255,0.05);">
            <ul style="margin:0; padding-left:1.5rem; font-size:0.95rem;">
                <li style="margin-bottom:0.4rem;">Apply fertilizer when water level is suitable for {soil_type} soil logic.</li>
                <li style="margin-bottom:0.4rem;">Do not apply before heavy rain.</li>
                {f'<li style="margin-bottom:0.4rem;">For {irrigation} irrigation, ensure proper management to avoid nutrient leaching.</li>' if irrigation else ''}
                {f'<li style="margin-bottom:0.4rem; color:#fbbf24;">Since you used {previous_fert} last season, balanced NPK this season is critically important to prevent nitrogen burn.</li>' if previous_fert else ''}
            </ul>
        </div>
        
    </div>
    """
        
    return html_output
