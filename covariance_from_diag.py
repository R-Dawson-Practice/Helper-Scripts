def covariance_from_diagonal(diag):
    cov = [0.0] * 36
    for i, val in enumerate(diag):
        cov[i * 6 + i] = float(val)
    return cov

def main():
    pose_cov_diag  = [0.01, 0.01, 1e6, 1e6, 1e6, 0.01]       

    covariance = covariance_from_diagonal(pose_cov_diag)
    print(covariance)
    
if __name__ == "__main__":
    main()