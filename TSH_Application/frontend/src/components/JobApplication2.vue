<template>
    <div>
        <NavBar />
        <Button label="< Back" class="mt-2 mx-2"
        style="border-radius: 20%; border: lightgrey; height: 35px; background-color: white; color: black "
        @click="$router.go('/')" />

        <div class="m-3 px-4">

            <h1 class="m-3">Example Job</h1>
            <hr>

            <div class="import-resume row" >
                <div class="col">
                    <h5 style="font-weight: 600; padding: 4px 0 0 0">🪄 Autofill Application</h5>
                    <p class="m-0" style="color: gray; padding: 2px 0">Save time by importing your resume.</p>
                </div>

                <div class="col" style="align-self: center; text-align: right;">
                    <FileUpload mode="basic" name="demo[]" url="/api/upload" :maxFileSize="1000000" @upload="onUpload" chooseLabel="Import Resume" cancelLabel="Cancel" />

                    <!-- <input type="file" name="resume"
                    accept="application/pdf, application/docx, application/doc" :maxFileSize="1000000"
                    style="background-color: rgba(211, 211, 211, 0); align-self: center; text-align: right; color: darkblue;" @change="onUpload($event, 'resume')" /> -->
                </div>

                <!-- v-if logic later -->
                <!-- <div class="col" style="align-self: center; text-align: right; max-width:40px; padding: 0 14px 0 0">
                    <ProgressSpinner style="width: 40px; height: 40px" strokeWidth="4"/>
                </div> -->
            </div>

            <br>

            <div class="row">
                <div class="col-3"></div>
                <div class="col" style="color: gray; font-size:smaller">
                    <span style="color: red;">*</span>
                    Required Information
                </div>
                <div class="col-3"></div>
            </div>

            <br>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <h4>Personal Information</h4>
                    <hr>
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="firstname" style="display: block">First Name <span style="color: red;">*</span></label>
                    <InputText id="firstname" v-model="fName" style="width: 300px" />
                </div>
                <div class="col">
                    <label for="lName" style="display: block"> Last Name <span style="color: red;">*</span></label>
                    <InputText v-model="lName" id="lName" style="width: 300px" />
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="email">Email <span style="color: red;">*</span></label>
                    <InputText v-model="email" @input="emailInput" id="email" style="width: 300px" />
                </div>
                <div class="col">
                    <label for="contact">Contact Number <span style="color: red;">*</span></label>
                    <InputText v-model="number" id="number" style="width: 300px" />
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <label for="school">School <span style="color: red;">*</span></label>
                    <InputText v-model="school" id="school" style="width: 300px" />
                </div>
                <div class="col">
                    <label for="course">Course of Study <span style="color: red;">*</span></label>
                    <InputText v-model="course" id="course" style="width: 300px" />
                </div>
                <div class="col-3"></div>
            </div>

            <br>

            <div class="row">
                <div class="col-3"></div>
                <div class="col">
                    <h4>Additional Documents</h4>
                    <hr>
                </div>
                <div class="col-3"></div>
            </div>

            <div class="row">
                <div class="col"></div>
                <div class="col">
                    <label for="transcript">Transcript <span style="color: red;">*</span></label>
                </div>
                <div class="col" style="text-align: right">
                    <FileUpload class="upload" mode="basic" name="demo[]" url="/api/upload" :maxFileSize="1000000" @upload="onUpload" chooseLabel="Upload" cancelLabel="Cancel" />
                </div>
                <div class="col"></div>
            </div>
            
            <br>

            <div class="row">
                <div class="col"></div>
                <div class="col" >
                    <label for="refLetter">Reference Letter</label>
                </div>
                <div class="col" style="text-align: right">
                    <FileUpload class="upload" mode="basic" name="demo[]" url="/api/upload" :maxFileSize="1000000" @upload="onUpload" chooseLabel="Upload" cancelLabel="Cancel"/>
                </div>
                <div class="col"></div>
            </div>

            <br>

            <div class="row">
                <div class="col-4">
            </div>
            <div class="col-2 justify-content-centre">
                <Button label="Cancel"
                 style="border-radius: 50px; background-color: gray; width: 150px" />
            </div>
            <div class="col-2 justify-content-centre">
                <Button label="Preview" 
                style="border-radius: 50px; background-color: darkblue; width: 150px" />
            </div>
            <div class="col-4"></div>   
          
            </div>

        </div>

    </div>
</template>

<script>
import NavBar from './NavBar.vue';

export default {
    components: {
        NavBar,
    }
}
</script>

<style>
.import-resume{
    padding: 20px;
    border-radius: 5px;
    box-shadow: 1px 1px 1px 1px #888888;
    width: 50%;
    margin: auto;
    background-color: #f5f5f5;
}
.p-button.p-component.p-fileupload-choose.upload {
    font-size: small;
    padding: 5px 10px;
    
}
</style>