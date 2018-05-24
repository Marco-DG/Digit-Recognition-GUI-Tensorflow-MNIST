# ==============================================================================
#   copyright (C) 2018 De Groskovskaja Marco
#
#   Licensed under the Apache License, Version 2.0;
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# ==============================================================================


import os.path
import shutil

import performRecognition
import prepareImage


def get_predictions(argv):
    
    if os.path.exists("./extracted_img"):
        shutil.rmtree("./extracted_img")
        os.makedirs("./extracted_img")
    else:
        os.makedirs("./extracted_img")

    digits = prepareImage.imageprepare(argv)
    predictions = performRecognition.predictint(digits)

    i=0
    for predicted in predictions:
        print ("Index["+str(i)+"] " + '\t'+ "Predicted number:  " + str(predicted))
        i = i+1

    return predictions
