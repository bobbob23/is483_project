let rootURL = "http://localhost:5000"

export const getAllJobListing = rootURL + "/job_listing_list"
export const getJobListing = rootURL + "/job_listing"
export const createJobListing = rootURL + "/new_job_listing"
export const getAllActiveJob = rootURL + "/active_job_listing_list"
export const editJobListing = rootURL + "/edit_job_listing"
export const deleteJobListing = rootURL + "/delete_job_listing"

export const createApplicant = rootURL + "/new_applicant"
export const createApplicantFiles = rootURL + "/new_applicant_files"
export const createTempFile = rootURL + "/post_file"

export const getAllApplicantStatus = rootURL + "/all_applicant_status"
export const getAllApplicant = rootURL + "/all_applicant_details"
export const getAllApplicantByJobID = rootURL + "/all_applicants"
export const editApplicantStatus = rootURL + "/edit_applicant_status"
export const getApplicantDetails = rootURL + "/applicant_details"
export const getApplicantFiles = rootURL + "/applicant_files"
export const getAllUnprocessedApplicant = rootURL + "/unprocessed_applicant_details"

// dashboard APIs
export const getDashboardDepartmentJobID = rootURL + "/department"
export const getDashboardDepartment = rootURL + "/manager/"
export const getDashboardJobID = rootURL + "/dashboard/"
export const getDashboardAllHRJobID = rootURL + "/job_ids"
export const getDashboardHRInfo = rootURL + "/HR"

// Autofill APIs
export const getAutofill = rootURL + "/autofill"

// Score API
export const getScoreDetails = rootURL + "/score_details/"