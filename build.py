import os
import sys

import RealtimeAppBuilder

config = {}

config["Project"] = \
   {
      "Name"                      : "ResponseModifier",
      "Version"                   : "v1.0.00-r5.3",
      "BuildNumber"               : "00000"
   }

#------------------------------------------------------------------------------#
# BuildEnvironment   
#------------------------------------------------------------------------------#
config["BuildEnvironment"] = \
   {
      "JDKHome"                   : "C:\Program Files\Postilion\realtime\jdk",
      "OutputDir"                 : ".\\build"
   }


   
   
config["Events"] = \
   {
      "EventResourceFile"         : ".\\resources\\events\\events.er",
      "EventsPackage"             : "postilion.realtime.responsemodifier.eventrecorder",
      "EventIdPackage"            : "postilion.realtime.responsemodifier",
      "EventIdClassName"          : "EventId",
	  "Condition"                 : "True"
   }   

#------------------------------------------------------------------------------#
# Java    
#------------------------------------------------------------------------------#
config["Java"] = \
   {
      "BasePackage"          : "postilion.realtime.responsemodifier",
      "SourceDirs"           : \
         [
            (".\\source\\java", RealtimeAppBuilder.INCLUDE_RECURSE)
         ],      
         "RegisteredClasses"         : \
         [
            ("postilion.realtime.responsemodifier.ResponseModifier")
         ]
   }

   
   
config["Database"] = \
   [
      (
         "realtime",
         {
            "CreateDatabase"           : False,
            "CreateDatabaseRegistry"   : False,

            "SourceDirs"       : \
               [
                   				(".\\source\\sql", RealtimeAppBuilder.INCLUDE_NO_RECURSE),
                                (".\\build\\sql\\support_events", RealtimeAppBuilder.INCLUDE_NO_RECURSE),
                                (".\\build\\sql\\data_upgrade", RealtimeAppBuilder.INCLUDE_NO_RECURSE)
               ],
            "UpgradeData"  :  \
               [
                     ("cfg_custom_classes",
                        [
                       ("INSERT", ("unique_name",), ("unique_name","category","display_name","class_name","parameters","description"), ("'NODE INTEGRATION:IDResponseModifier'", "'NODE INTEGRATION'", "'ID ResponseModifier'", "'postilion.realtime.responsemodifier.ResponseModifier'", "NULL", "'Integration Driver que modifica un mensaje segun las condiciones del mensaje recibido.'"))
                         ],
                     ),
               ],
         }
      )
   ]     
   
   
config["JavaDoc"] = \
   {
      "Title"                     : "ResponseModifier " + config["Project"]["Version"],
      "SourceDirs"                  : \
         [
            "./source/java",
            "./build/java",
         ],
      "Packages"                  : \
         [
            ("postilion.realtime.responsemodifier", RealtimeAppBuilder.INCLUDE_RECURSE)
         ],
      "Archive"                   : "javadoc"
   }

config["Documentation"] = \
   {
      "releasenotes"              : 
         {                    
            "Name"                : "ResponseModifier Release Notes",
            "Type"                : "CHM",
            "SourceDir"           : "doc\\releasenotes",
            "Project"             : "rn_ResponseModifier"
         },
	  "userguide"                 : 
         {                    
            "Name"                : "ResponseModifier User Guide",
            "Type"                : "CHM",
            "SourceDir"           : "doc\\userguide",
            "Project"             : "ug_ResponseModifier",
         }
	 }
  
	 	  
config["Content"] = \
   {
         "ClassFiles"	: \
            [
               ("INSTALL", "postilion.realtime.responsemodifier.*", ".\\build\\classes\\", "${postilion.dir}\\realtime\\java\\classes\\"),
            ]
         
      
    }

#------------------------------------------------------------------------------#
# Release									 #
#------------------------------------------------------------------------------#
config["Release"] = \
   {
      "Editions"              : ["Standard"],
      "Packaging"             : \
         {
            "Standard"  : \
               [
                  (RealtimeAppBuilder.WINDOWS_ONLY,"build\\install\\standard_edition\\setup.exe", "setup.exe"),
				  (RealtimeAppBuilder.WINDOWS_ONLY,"build\doc\\rn_ResponseModifier.chm", "doc\\rn_ResponseModifier.chm"),
				  (RealtimeAppBuilder.WINDOWS_ONLY,"build\doc\\ug_ResponseModifier.chm", "doc\\ug_ResponseModifier.chm")
               ]
         },
     }

#==============================================================================#
# Realtime Framework Builder										          #
#==============================================================================#

# Get the target and any target arguments that are present
target = RealtimeAppBuilder.getTargetName(sys.argv)
target_args = RealtimeAppBuilder.getTargetArguments(sys.argv)
   
# Build the target project.
RealtimeAppBuilder.RealtimeAppBuilder(config).buildProject(build_target=target, build_target_args=target_args)
