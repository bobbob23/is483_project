let rootURL = "http://localhost:8000"

export const getAllJobListing = rootURL + "/job_listing_list"
export const getJobListing = rootURL + "/job_listing"
export const createJobListing = rootURL + "/new_job_listing"
export const getAllActiveJob = rootURL + "/active_job_listing_list"

export const createApplicant = rootURL + "/new_applicant"
export const createApplicantFiles = rootURL + "/new_applicant_files"

export const getAllApplicantStatus = rootURL + "/all_applicant_status"
export const getAllApplicant = rootURL + "/all_applicant_details"
export const getAllApplicantByJobID = rootURL + "/all_applicants"
export const editApplicantStatus = rootURL + "/edit_applicant_status"