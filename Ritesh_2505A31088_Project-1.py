import math
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mechanical Engineering Calculator",
    page_icon="⚙️",
    layout="centered",
)

st.title("⚙️ Mechanical Engineering Calculator")
st.markdown(
    "Select a category from the sidebar and choose the formula you want to"
    " calculate."
)

# ============================================
# SIDEBAR NAVIGATION
# ============================================

st.sidebar.title("Navigation")
category = st.sidebar.selectbox(
    "Select Engineering Category",
    [
        "Mechanics",
        "Strength of Materials",
        "Thermodynamics",
        "Fluid Mechanics",
        "Thermal Engineering",
        "Machine Design",
    ],
)

# ============================================
# 1. MECHANICS
# ============================================
if category == "Mechanics":
  st.header("1. Mechanics")
  sub_choice = st.selectbox(
      "Choose Operation", ["Force", "Work", "Power", "Kinetic Energy"]
  )

  if sub_choice == "Force":
    st.subheader("Force Calculation ($F = m \cdot a$")
    mass = st.number_input("Enter mass (kg):", min_value=0.001, value=10.0)
    acceleration = st.number_input(
        "Enter acceleration ($m/s^2$):", min_value=0.001, value=9.81
    )
    if st.button("Calculate Force"):
      f = mass * acceleration
      st.success(f"**Force:** {f:.2f} N")

  elif sub_choice == "Work":
    st.subheader("Work Done ($W = F \cdot d$)")
    force_val = st.number_input("Enter force (N):", min_value=0.001, value=50.0)
    distance = st.number_input("Enter distance (m):", min_value=0.001, value=5.0)
    if st.button("Calculate Work"):
      w = force_val * distance
      st.success(f"**Work:** {w:.2f} J")

  elif sub_choice == "Power":
    st.subheader("Power ($P = W / t$)")
    work_val = st.number_input(
        "Enter work done (J):", min_value=0.001, value=1000.0
    )
    time_val = st.number_input("Enter time (s):", min_value=0.001, value=10.0)
    if st.button("Calculate Power"):
      p = work_val / time_val
      st.success(f"**Power:** {p:.2f} W")

  elif sub_choice == "Kinetic Energy":
    st.subheader("Kinetic Energy ($KE = \frac{1}{2} m v^2$)")
    mass = st.number_input("Enter mass (kg):", min_value=0.001, value=10.0)
    velocity = st.number_input(
        "Enter velocity (m/s):", min_value=0.0, value=15.0
    )
    if st.button("Calculate Kinetic Energy"):
      ke = 0.5 * mass * velocity**2
      st.success(f"**Kinetic Energy:** {ke:.2f} J")

# ============================================
# 2. STRENGTH OF MATERIALS
# ============================================
elif category == "Strength of Materials":
  st.header("2. Strength of Materials")
  sub_choice = st.selectbox(
      "Choose Operation", ["Stress", "Strain", "Young's Modulus"]
  )

  if sub_choice == "Stress":
    st.subheader("Stress ($\sigma = F / A$)")
    force_val = st.number_input(
        "Enter force (N):", min_value=0.001, value=5000.0
    )
    area = st.number_input(
        "Enter area ($mm^2$):", min_value=0.001, value=100.0
    )
    if st.button("Calculate Stress"):
      stress_val = force_val / area
      st.success(f"**Stress:** {stress_val:.2f} MPa")

  elif sub_choice == "Strain":
    st.subheader("Strain ($\epsilon = \Delta L / L_0$)")
    change_length = st.number_input(
        "Enter change in length (mm):", min_value=0.001, value=0.5
    )
    original_length = st.number_input(
        "Enter original length (mm):", min_value=0.001, value=200.0
    )
    if st.button("Calculate Strain"):
      strain_val = change_length / original_length
      st.success(f"**Strain:** {strain_val:.6f}")

  elif sub_choice == "Young's Modulus":
    st.subheader("Young's Modulus ($E = \sigma / \epsilon$)")
    stress_val = st.number_input(
        "Enter stress (MPa):", min_value=0.001, value=200.0
    )
    strain_val = st.number_input("Enter strain:", min_value=0.000001, value=0.001)
    if st.button("Calculate Young's Modulus"):
      e = stress_val / strain_val
      st.success(
          f"**Young's Modulus:** {e:.2f} MPa ({e / 1000:.2f} GPa)"
      )

# ============================================
# 3. THERMODYNAMICS
# ============================================
elif category == "Thermodynamics":
  st.header("3. Thermodynamics")
  sub_choice = st.selectbox(
      "Choose Operation",
      ["Heat Transfer", "Work Done", "Thermal Efficiency"],
  )

  if sub_choice == "Heat Transfer":
    st.subheader("Heat Transfer ($Q = m \cdot c \cdot \Delta T$)")
    mass = st.number_input("Enter mass (kg):", min_value=0.001, value=2.0)
    spec_heat = st.number_input(
        "Enter specific heat (J/kg.K):", min_value=0.001, value=4186.0
    )
    temp_change = st.number_input(
        "Enter temperature change (K):", min_value=0.001, value=50.0
    )
    if st.button("Calculate Heat Transfer"):
      q = mass * spec_heat * temp_change
      st.success(
          f"**Heat Transfer:** {q:.2f} J ({q / 1000:.2f} kJ)"
      )

  elif sub_choice == "Work Done":
    st.subheader("Thermodynamic Work ($W = P \cdot \Delta V$)")
    pressure = st.number_input(
        "Enter pressure (Pa):", min_value=0.001, value=101325.0
    )
    vol_change = st.number_input(
        "Enter change in volume ($m^3$):", min_value=0.001, value=0.5
    )
    if st.button("Calculate Work Done"):
      w = pressure * vol_change
      st.success(
          f"**Work Done:** {w:.2f} J ({w / 1000:.2f} kJ)"
      )

  elif sub_choice == "Thermal Efficiency":
    st.subheader("Thermal Efficiency ($\eta = (Q_{in} - Q_{out}) / Q_{in}$)")
    heat_in = st.number_input(
        "Enter heat supplied (kJ):", min_value=0.001, value=500.0
    )
    heat_rej = st.number_input("Enter heat rejected (kJ):", min_value=0.0, value=200.0)
    if st.button("Calculate Efficiency"):
      if heat_rej >= heat_in:
        st.error("Heat rejected must be less than heat supplied.")
      else:
        eff = ((heat_in - heat_rej) / heat_in) * 100
        st.success(f"**Thermal Efficiency:** {eff:.2f}%")

# ============================================
# 4. FLUID MECHANICS
# ============================================
elif category == "Fluid Mechanics":
  st.header("4. Fluid Mechanics")
  sub_choice = st.selectbox(
      "Choose Operation",
      ["Pressure", "Reynolds Number", "Flow Velocity", "Discharge"],
  )

  if sub_choice == "Pressure":
    st.subheader("Pressure ($P = F / A$)")
    force_val = st.number_input("Enter force (N):", min_value=0.001, value=100.0)
    area = st.number_input(
        "Enter area ($m^2$):", min_value=0.001, value=2.0
    )
    if st.button("Calculate Pressure"):
      p = force_val / area
      st.success(
          f"**Pressure:** {p:.2f} Pa ({p / 1000:.2f} kPa)"
      )

  elif sub_choice == "Reynolds Number":
    st.subheader("Reynolds Number ($Re = \rho v D / \mu$)")
    density = st.number_input(
        "Enter fluid density ($kg/m^3$):", min_value=0.001, value=998.0
    )
    velocity = st.number_input(
        "Enter flow velocity (m/s):", min_value=0.001, value=1.5
    )
    diameter = st.number_input(
        "Enter pipe diameter (m):", min_value=0.001, value=0.05
    )
    viscosity = st.number_input(
        "Enter dynamic viscosity (Pa.s):", min_value=0.000001, value=0.001
    )
    if st.button("Calculate Reynolds Number"):
      re = (density * velocity * diameter) / viscosity
      flow_type = (
          "Laminar"
          if re < 2300
          else ("Transitional" if re <= 4000 else "Turbulent")
      )
      st.success(f"**Reynolds Number:** {re:.2f} — **Flow Type:** {flow_type}")

  elif sub_choice == "Flow Velocity":
    st.subheader("Flow Velocity ($v = Q / A$)")
    discharge_val = st.number_input(
        "Enter discharge ($m^3/s$):", min_value=0.001, value=0.05
    )
    area = st.number_input(
        "Enter cross-sectional area ($m^2$):", min_value=0.001, value=0.1
    )
    if st.button("Calculate Velocity"):
      vel = discharge_val / area
      st.success(f"**Flow Velocity:** {vel:.2f} m/s")

  elif sub_choice == "Discharge":
    st.subheader("Discharge ($Q = A \cdot v$)")
    area = st.number_input(
        "Enter cross-sectional area ($m^2$):", min_value=0.001, value=0.1
    )
    velocity = st.number_input(
        "Enter flow velocity (m/s):", min_value=0.001, value=2.0
    )
    if st.button("Calculate Discharge"):
      q = area * velocity
      st.success(f"**Discharge:** {q:.4f} $m^3/s$")

# ============================================
# 5. THERMAL ENGINEERING
# ============================================
elif category == "Thermal Engineering":
  st.header("5. Thermal Engineering")
  sub_choice = st.selectbox(
      "Choose Operation",
      ["Heat Conduction", "COP (Coefficient of Performance)", "Heat Engine Efficiency"],
  )

  if sub_choice == "Heat Conduction":
    st.subheader("Heat Conduction Rate ($Q = k A \Delta T / L$)")
    k_val = st.number_input(
        "Enter thermal conductivity $k$ (W/m.K):", min_value=0.001, value=40.0
    )
    area = st.number_input(
        "Enter area ($m^2$):", min_value=0.001, value=1.5
    )
    temp_diff = st.number_input(
        "Enter temperature difference (K):", min_value=0.001, value=30.0
    )
    thickness = st.number_input(
        "Enter thickness (m):", min_value=0.001, value=0.02
    )
    if st.button("Calculate Heat Conduction"):
      q = (k_val * area * temp_diff) / thickness
      st.success(f"**Heat Conduction Rate:** {q:.2f} W")

  elif sub_choice == "COP (Coefficient of Performance)":
    st.subheader("Coefficient of Performance ($COP = Q_L / W_in$)")
    cooling_effect = st.number_input(
        "Enter cooling effect (kJ):", min_value=0.001, value=350.0
    )
    work_input = st.number_input(
        "Enter work input (kJ):", min_value=0.001, value=100.0
    )
    if st.button("Calculate COP"):
      cop = cooling_effect / work_input
      st.success(f"**COP:** {cop:.2f}")

  elif sub_choice == "Heat Engine Efficiency":
    st.subheader("Heat Engine Efficiency ($\eta = (Q_{in} - Q_{out}) / Q_{in}$)")
    heat_in = st.number_input(
        "Enter heat supplied (kJ):", min_value=0.001, value=1000.0
    )
    heat_rej = st.number_input("Enter heat rejected (kJ):", min_value=0.0, value=600.0)
    if st.button("Calculate Efficiency"):
      if heat_rej >= heat_in:
        st.error("Heat rejected must be less than heat supplied.")
      else:
        eff = ((heat_in - heat_rej) / heat_in) * 100
        st.success(f"**Heat Engine Efficiency:** {eff:.2f}%")

# ============================================
# 6. MACHINE DESIGN
# ============================================
elif category == "Machine Design":
  st.header("6. Machine Design")
  sub_choice = st.selectbox(
      "Choose Operation", ["Torque", "Shaft Power", "Shaft Diameter"]
  )

  if sub_choice == "Torque":
    st.subheader("Torque ($T = F \cdot r$)")
    force_val = st.number_input("Enter force (N):", min_value=0.001, value=250.0)
    radius = st.number_input(
        "Enter radius / lever arm (m):", min_value=0.001, value=0.4
    )
    if st.button("Calculate Torque"):
      t = force_val * radius
      st.success(f"**Torque:** {t:.2f} N.m")

  elif sub_choice == "Shaft Power":
    st.subheader("Shaft Power ($P = 2 \pi N T / 60$)")
    torque_val = st.number_input(
        "Enter torque (N.m):", min_value=0.001, value=150.0
    )
    rpm = st.number_input("Enter speed (RPM):", min_value=0.001, value=1440.0)
    if st.button("Calculate Shaft Power"):
      p = (2 * math.pi * rpm * torque_val) / 60
      st.success(
          f"**Shaft Power:** {p:.2f} W ({p / 1000:.2f} kW)"
      )

  elif sub_choice == "Shaft Diameter":
    st.subheader("Shaft Diameter ($T = \frac{\pi}{16} \tau d^3$)")
    torque_val = st.number_input(
        "Enter torque (N.m):", min_value=0.001, value=200.0
    )
    allowable_shear = st.number_input(
        "Enter allowable shear stress (MPa):", min_value=0.001, value=50.0
    )
    if st.button("Calculate Shaft Diameter"):
      torque_nmm = torque_val * 1000
      diameter = (
          (16 * torque_nmm) / (math.pi * allowable_shear)
      ) ** (1 / 3)
      st.success(f"**Shaft Diameter:** {diameter:.2f} mm")
