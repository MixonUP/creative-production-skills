"""Small original mathematical reference lab. Standard library only; no live tools."""
import argparse
import csv
import hashlib
import json
import math
import platform
import random
from pathlib import Path

VERSION = '1.0.0'


def number(value, name, positive=False, nonnegative=False):
    if isinstance(value, bool):
        raise ValueError(f'{name}: boolean is not a number')
    value = float(value)
    if not math.isfinite(value) or (positive and value <= 0) or (nonnegative and value < 0):
        raise ValueError(f'{name}: outside domain')
    return value


def count(value, name, low, high):
    value = number(value, name)
    if not value.is_integer() or not low <= value <= high:
        raise ValueError(f'{name}: integer {low}..{high} required')
    return int(value)


def smootherstep(u):
    u = min(1.0, max(0.0, number(u, 'u')))
    return u*u*u*(u*(u*6-15)+10)


def disk_points(radius, n, seed):
    radius = number(radius, 'radius', positive=True)
    n = count(n, 'n', 1, 100000)
    seed = count(seed, 'seed', 0, 2**32-1)
    rng = random.Random(seed)
    points = []
    for _ in range(n):
        r, a = radius*math.sqrt(rng.random()), math.tau*rng.random()
        points.append((r*math.cos(a), r*math.sin(a)))
    return points


def spaced_points(width, height, n, distance, seed, attempts=10000):
    """Bounded naive rejection baseline; not Bridson and not maximal packing."""
    width, height = number(width, 'width', positive=True), number(height, 'height', positive=True)
    distance = number(distance, 'distance', positive=True)
    n = count(n, 'n', 1, 2000)
    attempts = count(attempts, 'attempts', 1, 1000000)
    seed = count(seed, 'seed', 0, 2**32-1)
    rng, points = random.Random(seed), []
    for _ in range(attempts):
        candidate = (rng.random()*width, rng.random()*height)
        if all(math.dist(candidate, p) >= distance for p in points):
            points.append(candidate)
            if len(points) == n:
                return points
    raise ValueError(f'Attempt budget exhausted: accepted {len(points)} of {n}; no full solution')


def chirp_phase(t, f0, f1, duration):
    t = number(t, 't', nonnegative=True)
    duration = number(duration, 'duration', positive=True)
    f0, f1 = number(f0, 'f0', nonnegative=True), number(f1, 'f1', nonnegative=True)
    if t > duration:
        raise ValueError('t exceeds chirp duration')
    return math.tau*(f0*t+(f1-f0)*t*t/(2*duration))


def decay(t, t60):
    t, t60 = number(t, 't', nonnegative=True), number(t60, 't60', positive=True)
    return math.exp(-math.log(1000)*t/t60)


def dispersion(q, c, b):
    q, c, b = number(q, 'q', nonnegative=True), number(c, 'c', positive=True), number(b, 'B', nonnegative=True)
    return c*q*math.sqrt(1+b*q*q)


def group_speed(q, c, b):
    q, c, b = number(q, 'q', nonnegative=True), number(c, 'c', positive=True), number(b, 'B', nonnegative=True)
    return c*(1+2*b*q*q)/math.sqrt(1+b*q*q)


def stiff_mode(n, first_hz, beta):
    n = count(n, 'mode index', 1, 100000)
    first_hz = number(first_hz, 'first_hz', positive=True)
    beta = number(beta, 'beta', nonnegative=True)
    return n*first_hz*math.sqrt((1+beta*n*n)/(1+beta))


def damper(x, goal, half_life, dt):
    x, goal = number(x, 'x'), number(goal, 'goal')
    half_life, dt = number(half_life, 'half_life', positive=True), number(dt, 'dt', nonnegative=True)
    return goal+(x-goal)*2**(-dt/half_life)


def spring(x, velocity, goal, omega, dt):
    x, velocity, goal = number(x, 'x'), number(velocity, 'velocity'), number(goal, 'goal')
    omega, dt = number(omega, 'omega', positive=True), number(dt, 'dt', nonnegative=True)
    displacement, e = x-goal, math.exp(-omega*dt)
    j = velocity+omega*displacement
    return goal+(displacement+j*dt)*e, (velocity-omega*j*dt)*e


def ik2(a, b, x, y, branch=1):
    a, b, x, y = number(a, 'a', positive=True), number(b, 'b', positive=True), number(x, 'x'), number(y, 'y')
    if branch not in (-1, 1):
        raise ValueError('branch must be -1 or 1')
    r = math.hypot(x, y)
    tolerance = 1e-12*max(1.0, a, b, r)
    if r < abs(a-b)-tolerance or r > a+b+tolerance:
        raise ValueError('Unreachable target')
    if r <= tolerance and abs(a-b) <= tolerance:
        raise ValueError('Singular folded pose: requires a chosen orientation')
    cosine = min(1.0, max(-1.0, (r*r-a*a-b*b)/(2*a*b)))
    t2 = branch*math.acos(cosine)
    t1 = math.atan2(y, x)-math.atan2(b*math.sin(t2), a+b*math.cos(t2))
    return t1, t2


def cfg(unconditional, conditional, scale):
    u, c, s = number(unconditional, 'unconditional'), number(conditional, 'conditional'), number(scale, 'scale')
    return u+s*(c-u)


def verify():
    tests = []
    def check(name, passed, measured=None):
        tests.append({'id': name, 'passed': bool(passed), 'measured': measured})
    check('easing_endpoints_and_range', smootherstep(-1) == 0 and smootherstep(2) == 1 and all(0 <= smootherstep(i/100) <= 1 for i in range(101)))
    h = 1e-4
    slopes = [abs((smootherstep(h)-smootherstep(0))/h), abs((smootherstep(1)-smootherstep(1-h))/h)]
    curvature = [abs((smootherstep(2*h)-2*smootherstep(h)+smootherstep(0))/(h*h)), abs((smootherstep(1)-2*smootherstep(1-h)+smootherstep(1-2*h))/(h*h))]
    check('easing_endpoint_derivatives', max(slopes)<1e-6 and max(curvature)<0.01, {'max_slope':max(slopes), 'max_curvature':max(curvature)})
    disk = disk_points(2, 16000, 417)
    mean_r2 = sum(x*x+y*y for x,y in disk)/len(disk)
    check('disk_uniform_area_second_moment', abs(mean_r2-2)<0.04, {'mean_r2':mean_r2, 'expected':2, 'tolerance':0.04})
    check('disk_radius_bound', max(math.hypot(*p) for p in disk)<=2)
    points = spaced_points(20, 20, 80, 1, 471)
    min_spacing = min(math.dist(p,q) for i,p in enumerate(points) for q in points[i+1:])
    check('scatter_spacing_and_count', len(points)==80 and min_spacing>=1, {'min_spacing_m':min_spacing})
    check('random_seed_reproduction', disk==disk_points(2,16000,417) and points==spaced_points(20,20,80,1,471))
    try:
        spaced_points(1, 1, 3, 2, 5, 50)
        rejected = False
    except ValueError:
        rejected = True
    check('impossible_scatter_stops', rejected)
    errors = []
    for t in (0.1,0.4,0.8,1.4):
        h = 1e-6
        measured = (chirp_phase(t+h,200,1400,1.6)-chirp_phase(t-h,200,1400,1.6))/(2*h*math.tau)
        expected = 200+750*t
        errors.append(abs(measured-expected))
    check('phase_derivative_matches_frequency', max(errors)<1e-5, {'max_error_hz':max(errors)})
    check('decay_T60_amplitude', math.isclose(decay(0.8,0.8),0.001,rel_tol=1e-12) and decay(0,0.8)==1)
    errors = []
    for q in (1, 10, 100):
        h = 1e-4
        numerical = (dispersion(q+h,50,0.0004)-dispersion(q-h,50,0.0004))/(2*h)
        errors.append(abs(numerical-group_speed(q,50,0.0004)))
    check('dispersion_group_velocity_derivative', max(errors)<1e-6, {'max_error_m_s':max(errors)})
    check('stiff_string_limiting_cases', all(stiff_mode(n,110,0)==n*110 for n in range(1,9)) and stiff_mode(1,110,0.02)==110 and stiff_mode(8,110,0.02)>880)
    outcomes = []
    for fps in (24,30,60,120):
        x = 10
        for _ in range(fps):
            x = damper(x,2,0.25,1/fps)
        outcomes.append(x)
    check('damper_fps_and_known_half_lives', max(abs(x-2.5) for x in outcomes)<1e-12, outcomes)
    direct = spring(10,-2,3,6,1)
    errors = []
    for fps in (24,30,60,120):
        x, v = 10,-2
        for _ in range(fps):
            x,v = spring(x,v,3,6,1/fps)
        errors.append(max(abs(x-direct[0]),abs(v-direct[1])))
    check('spring_constant_target_semigroup', max(errors)<1e-12 and spring(10,-2,3,6,0)==(10,-2), {'max_error':max(errors)})
    errors = []
    for x,y in ((1.2,0.3),(-0.8,0.7),(-1,-0.4),(0,-1.2),(1.8,0)):
        for branch in (-1,1):
            t1,t2 = ik2(1,0.8,x,y,branch)
            reconstructed = (math.cos(t1)+0.8*math.cos(t1+t2),math.sin(t1)+0.8*math.sin(t1+t2))
            errors.append(math.dist((x,y),reconstructed))
    check('ik_forward_kinematics_both_branches', max(errors)<1e-12, {'max_endpoint_error_m':max(errors)})
    bad = [lambda: ik2(1,0.8,3,0), lambda: ik2(1,0.8,0.01,0), lambda: ik2(1,1,0,0), lambda: decay(1,0), lambda: smootherstep(float('nan')), lambda: chirp_phase(2,200,400,1), lambda: dispersion(1,50,-1)]
    rejected = 0
    for fn in bad:
        try:
            fn()
        except ValueError:
            rejected += 1
    check('domain_and_singularity_rejection', rejected==len(bad), {'rejected':rejected})
    check('cfg_conventions_only_algebra', cfg(4,10,0)==4 and cfg(4,10,1)==10 and cfg(4,10,3)==(1+2)*10-2*4)
    if not all(item['passed'] for item in tests):
        raise RuntimeError(json.dumps(tests,indent=2))
    return tests


def write_csv(path, header, rows):
    with path.open('w', newline='', encoding='utf-8') as stream:
        writer = csv.writer(stream)
        writer.writerow(header)
        writer.writerows(rows)


def export_lab(output):
    if output.exists():
        raise FileExistsError('Choose a new evidence revision; output already exists')
    tests = verify()
    output.mkdir(parents=True, exist_ok=False)
    write_csv(output/'disk_points.csv', ['x_m','y_m'], disk_points(2,2048,417))
    write_csv(output/'spaced_points.csv', ['x_m','y_m'], spaced_points(20,20,80,1,471))
    write_csv(output/'camera_curve.csv', ['index','time_s','distance_m','kind'], [(j,j/24,3*smootherstep(j/96),'frame_start' if j<96 else 'end_boundary') for j in range(97)])
    write_csv(output/'audio_control.csv', ['time_s','frequency_hz','phase_rad','amplitude'], [(j/200,200+750*j/200,chirp_phase(j/200,200,1400,1.6),decay(j/200,0.8)) for j in range(321)])
    artifacts = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(output.iterdir()) if p.is_file()}
    report = {'lab_version':VERSION, 'python':platform.python_version(), 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'tests':tests, 'passed':True, 'artifacts':artifacts, 'scope':'Selected reference implementations only; not all formulas, artistic quality or AI-model integration.', 'artistic_review':'not-run', 'live_tool_or_ai_integration':'not-run', 'camera_contract':{'duration_s':4,'fps':24,'frames':96,'rows':97,'end_boundary_is_not_an_extra_frame':True}, 'audio_control':'Control-rate CSV at 200 Hz, not an audio-rate waveform or playable WAV.'}
    (output/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(output.resolve()),'tests_passed':len(tests),'artifacts':len(artifacts),'integration':'not-run'}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,help='New evidence folder: run checks and export example CSVs')
    args = parser.parse_args()
    if args.out:
        export_lab(args.out)
    else:
        print(json.dumps({'tests':verify(),'passed':True},indent=2))
